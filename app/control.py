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

def Info_Alarmas_Variador1(valores):
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

def Info_Alarmas_Variador2(valores):
    valores = Componer_trip2(valores['trip2'])
    return(
        Card(
            Table(
                Tbody(
                    Tr(Td(H5('Mc-Fail')), Td(valores['Mc-Fail'])),
                    Tr(Td(H5('Encoder Error')), Td(valores['Encoder Error'])),
                    Tr(Td(H5('PTC')), Td(valores['PTC'])),
                    Tr(Td(H5('FAN TRIP')), Td(valores['FAN TRIP'])),
                    Tr(Td(H5('Param_Wr_Err')), Td(valores['Param_Wr_Err'])),
                    Tr(Td(H5('Pipe Fill Fit')), Td(valores['Pipe Fill Fit'])),
                    Tr(Td(H5('IO Board Fail')), Td(valores['IO Board Fail'])),
                    Tr(Td(H5('External Brake')), Td(valores['External Brake'])),
                    Tr(Td(H5('No Motor')), Td(valores['No Motor'])),
                    Tr(Td(H5('Slot 1 Fail')), Td(valores['Slot 1 Fail'])),
                    Tr(Td(H5('Slot 2 Fail')), Td(valores['Slot 2 Fail'])),
                    Tr(Td(H5('Slot 3 Fail')), Td(valores['Slot 3 Fail'])),
                )
            ),    
            header = (H4('Alertas del variador'))
            )
        )

def Info_Actual_Variador(valores):
    if valores['estado'] != '8193':
        estado_inversor = UkIcon("circle-play",25,25)
    else:
        estado_inversor = UkIcon("circle-pause",25,25)
    return(
        Card(
            Table(
                Tbody(
                    Tr(Td(H5('Estado')), Td(estado_inversor)),
                    Tr(Td(H5('Frecuencia Refrencia')), Td(str(valores['frecuencia_ref']) + " Hz")),
                    Tr(Td(H5('Frecuencia')), Td(str(valores['frecuencia']) + " Hz")),
                    Tr(Td(H5('Intensidad')), Td(str(valores['intensidad']) + " A")),
                    Tr(Td(H5('Tension')), Td(str(valores['tension']) + " V")),
                    Tr(Td(H5('Bus DC')), Td(str(valores['dc_bus']) + " V")),
                    Tr(Td(H5('RPM')), Td(str(valores['rpm']) + " rpm")),
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
    valores = [0] * 16
    for i in range(len(estado)):
        if estado[i] == '0':
            valores[i] = UkIcon("check")
        else:
            valores[i] = UkIcon("circle-x")
    listado_setpoint = {0: "Local", 1: "Start/Stop-1",2: "Start/Stop-2", 3: "RS485 integrated", 4: "Communications Option", 5: "PLC Option"}
    valor = {'Stop': valores[0], 'Forward': valores[1], 'Reverse': valores[2], 'Fault': valores[3], 'Emergency Stop': valores[4], 
             'Setpoint': listado_setpoint[int(estado[6])], 'Reference Frequency': valores[9], 'Network Error': valores[15]}
    return(valor)

def Componer_trip1(trip1):
    trip1 = '{0:016b}'.format(trip1)
    trip1 = trip1[::-1]
    valores = [0] * 16
    for i in range(len(trip1)):
        if trip1[i] == '0':
            valores[i] = UkIcon("check")
        else:
            valores[i] = UkIcon("circle-x")
    valor = {'OverLoad': valores[0], 'UnderLoad': valores[1], 'Inv OverLoad': valores[2], 'E-Thermal': valores[3], 'Ground Fault': valores[4], 
            'Out Ph Loss': valores[5], 'Input Ph Loss': valores[6], 'OverSpeed': valores[7], 'NTC': valores[9], 'OverCurrent': valores[10],
            'OverVoltage': valores[11], 'External Trip': valores[12], 'Short ARM': valores[13], 'OverHeat': valores[14], "Fuse Open": valores[15]}
    return(valor)

def Componer_trip2(trip2):
    trip2 = '{0:016b}'.format(trip2)
    trip2 = trip2[::-1]
    valores = [0] * 16
    for i in range(len(trip2)):
        if trip2[i] == '0':
            valores[i] = UkIcon("check")
        else:
            valores[i] = UkIcon("circle-x")
    valor = {'Mc-Fail': valores[0], 'Encoder Error': valores[1], 'PTC': valores[2], 'FAN TRIP': valores[3], 'Param_Wr_Err': valores[5], 
            'Pipe Fill Fit': valores[6], 'IO Board Fail': valores[7], 'External Brake': valores[8], 'No Motor': valores[9], 'Slot 1 Fail': valores[10],
            'Slot 2 Fail': valores[11], 'Slot 3 Fail': valores[12]}
    
    return(valor)