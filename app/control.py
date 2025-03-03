from fasthtml.common import *
from fasthtml.components import Uk_input_tag
from fasthtml.svg import *
from monsterui.all import *
import json

def Info_Control_variador():
    return(Card(
        Form(
            Table(
                Tbody(
                    Tr(Td(H5('Encender')), Td(Switch(checked=True, name="estado"))),
                    Tr(Td(H5('Frecuencia')), Td(LabelRange("",min=0, max=50, step=1, id="frecuencia", name="frecuencia"))),
                )
            ),
            Button("Enviar", hx_post="/control_variador")
            ),    
        header = (H4('Control variador'), 
            Subtitle('Control Via Modbus del Variador de Frecuencia'))
        )
    )

def Info_Avanzada_Variador():
    Lista_potencia = {0:0.75, 1:1.5, 2:2.2, 3:3.7, 4:5.5, 5:7.5, 6:11, 7:15, 8:18.5, 9:22, 10:30, 11:37,
        12:45, 13:55, 14:75}
    Lista_tension = {0:220, 1:400}
    with open('app/data/configuracion_variador.json') as f:
        valores = json.load(f)
        f.close()
    return(
        Card(
            Table(
                Tbody(
                    Tr(Td(H5('Potencia del variador')), Td(str(Lista_potencia[valores['potencia_variador']]) + " kW")),
                    Tr(Td(H5('Tensión de entrada')), Td(str(Lista_tension[valores['input_voltaje']]) + " V")),
                    Tr(Td(H5('Tiempo Aceleramiento')), Td(str(valores['acceleration_time']) + " s")),
                    Tr(Td(H5('Tiempo Desaceleramiento')), Td(str(valores['desacceleration_time']) + " s")),
                )
            ),    
            header = (H4('Información del variador'))
            )
        )

def Info_Alarmas_Variador():
    with open('app/data/configuracion_variador.json') as f:
        valores = json.load(f)
        f.close()
    return(
        Card(
            Table(
                Tbody(
                    Tr(Td(H5('Alarma 1')), Td(valores['trip1'])),
                    Tr(Td(H5('Alarma 2')), Td(valores['trip2'])),
                )
            ),    
            header = (H4('Alertas del variador'))
            )
        )

def Info_Actual_Variador(valores):
    return(
        Card(
            Table(
                Tbody(
                    Tr(Td(H5('Estado')), Td(UkIcon("circle", color="#ff0000"),)),
                    Tr(Td(H5('Frecuencia Refrencia')), Td(str(valores['frecuencia_ref']) + " Hz")),
                    Tr(Td(H5('Frecuencia')), Td(str(valores['frecuencia']) + " Hz")),
                    Tr(Td(H5('Intensidad')), Td(str(valores['intensidad']) + " A")),
                    Tr(Td(H5('Tension')), Td(str(valores['tension']) + " V")),
                    Tr(Td(H5('Bus DC')), Td(str(valores['dc_bus']) + " V")),
                )
            ),    
            header = (H4('Información Actual del variador'))
        )
    )