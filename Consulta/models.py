from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import Date, cast, extract, func
from datetime import datetime

from database import Base, session, engine

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

def new_register_variador(valores):
    registro = Variador(**valores) 
    session.add(registro)
    session.commit()