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

def Info_Alarmas_Variador(valores):
    valores = Componer_trip1(valores['trip1'])
    return(
        Card(
            Table(
                Tbody(
                    Tr(Td(H5('OverLoad')), Td(valores['OverLoad'])),
                    Tr(Td(H5('UnderLoad')), Td(valores['UnderLoad'])),
                    Tr(Td(H5('Inv OverLoad')), Td(valores['Inv OverLoad'])),
                    Tr(Td(H5('E-Thermal')), Td(valores['E-Thermal'])),
                    Tr(Td(H5('Ground Fault')), Td(valores['Ground Fault'])),
                    Tr(Td(H5('Out Ph Loss')), Td(valores['Out Ph Loss'])),
                    Tr(Td(H5('Input Ph Loss')), Td(valores['Input Ph Loss'])),
                    Tr(Td(H5('OverSpeed')), Td(valores['OverSpeed'])),
                    Tr(Td(H5('NTC')), Td(valores['NTC'])),
                    Tr(Td(H5('OverCurrent')), Td(valores['OverCurrent'])),
                    Tr(Td(H5('OverVoltage')), Td(valores['OverVoltage'])),
                    Tr(Td(H5('External Trip')), Td(valores['External Trip'])),
                    Tr(Td(H5('Short ARM')), Td(valores['Short ARM'])),
                    Tr(Td(H5('OverHeat')), Td(valores['OverHeat'])),
                    Tr(Td(H5('Fuse Open')), Td(valores['Fuse Open'])),
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

def Info_Estado(valores):
    valores = Componer_estado(valores['estado'])
    return(
        Card(
            Table(
                Tbody(
                    Tr(Td(H5('Stop')), Td(valores['Stop'])),
                    Tr(Td(H5('Forward')), Td(valores['Forward'])),
                    Tr(Td(H5('Reverse')), Td(valores['Reverse'])),
                    Tr(Td(H5('Fault')), Td(valores['Fault'])),
                    Tr(Td(H5('Emergency Stop')), Td(valores['Emergency Stop'])),
                    Tr(Td(H5('Setpoint')), Td(valores['Setpoint'])),
                    Tr(Td(H5('Reference Frequency')), Td(valores['Reference Frequency'])),
                    Tr(Td(H5('Network Error')), Td(valores['Network Error'])),
                )
            ),    
            header = (H4('Información Estado del variador'))
        )
    )

def Componer_estado(estado):
    estado = '{0:016b}'.format(estado)
    estado = estado[::-1]
    listado_setpoint = {0: "Local", 1: "Start/Stop-1",2: "Start/Stop-2", 3: "RS485 integrated", 4: "Communications Option", 5: "PLC Option"}
    valor = {'Stop': estado[0], 'Forward': estado[1], 'Reverse': estado[2], 'Fault': estado[3], 'Emergency Stop': estado[4], 
             'Setpoint': listado_setpoint[int(estado[6])], 'Reference Frequency': estado[9], 'Network Error': estado[15]}
    return(valor)

def Componer_trip1(trip1):
    trip1 = '{0:016b}'.format(trip1)
    trip1 = trip1[::-1]
    valor = {'OverLoad': trip1[0], 'UnderLoad': trip1[1], 'Inv OverLoad': trip1[2], 'E-Thermal': trip1[3], 'Ground Fault': trip1[4], 
            'Out Ph Loss': trip1[5], 'Input Ph Loss': trip1[6], 'OverSpeed': trip1[7], 'NTC': trip1[9], 'OverCurrent': trip1[10],
            'OverVoltage': trip1[11], 'External Trip': trip1[12], 'Short ARM': trip1[13], 'OverHeat': trip1[14], "Fuse Open": trip1[15]}
    return(valor)