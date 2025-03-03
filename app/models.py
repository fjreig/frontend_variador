from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import Date, cast, extract, func
from datetime import datetime
import pandas as pd
import datetime
import json

from app.database import Base, session, engine

class Variador(Base):
    __tablename__ = "variador"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime)
    frecuencia_ref = Column(Float)
    estado = Column(Integer)
    intensidad = Column(Float)
    frecuencia = Column(Float)
    tension = Column(Float)
    dc_bus = Column(Float)

def get_all():
    result = session.query(Variador).limit(5).all()
    return(result)

def get_last_value():
    result = session.query(Variador).order_by(Variador.id.desc()).first()
    valores = result.__dict__
    valores_fin = [
        {'Variable': 'Frecuencia Referencia', 'Valor': valores['frecuencia_ref'], 'Unidades': 'Hz', 'Fecha_Actualizacion': valores['fecha']},
        {'Variable': 'Frecuencia', 'Valor': valores['frecuencia'], 'Unidades': 'Hz', 'Fecha_Actualizacion': valores['fecha']},
        {'Variable': 'Intensidad', 'Valor': valores['intensidad'], 'Unidades': 'A', 'Fecha_Actualizacion': valores['fecha']},
        {'Variable': 'Tension', 'Valor': valores['tension'], 'Unidades': 'V', 'Fecha_Actualizacion': valores['fecha']},
        {'Variable': 'Bus DC', 'Valor': valores['dc_bus'], 'Unidades': 'V', 'Fecha_Actualizacion': valores['fecha']},
        {'Variable': 'Estado', 'Valor': valores['estado'], 'Unidades': '-', 'Fecha_Actualizacion': valores['fecha']},
    ]
    return(valores_fin)

## Consultas graficos
def get_df():
    today = datetime.date.today()
    results  = session.query(Variador).\
        filter(cast(Variador.fecha, Date) == today).\
        order_by(Variador.id.desc()).\
        all()
    df = pd.DataFrame([r.__dict__ for r in results])
    df = df.drop(columns=['_sa_instance_state'])
    return(df)

## Añadir nuevos registros
def new_register(valores):
    registro = Variador(
        fecha = str(datetime.datetime.now()),
        frecuencia_ref = valores['frecuencia_ref'],
        estado = valores['estado'],
        intensidad = valores['intensidad'],
        frecuencia = valores['frecuencia'],
        tension = valores['tension'],
        dc_bus = valores['dc_bus'],
        ) 
    session.add(registro)
    session.commit()