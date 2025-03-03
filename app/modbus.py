import pymodbus.client as ModbusClient
from pymodbus import  FramerType, ModbusException, pymodbus_apply_logging_config
from app.config import settings
import json
import os

client: ModbusClient.ModbusBaseSyncClient
client = ModbusClient.ModbusTcpClient(
    settings.MODBUS_HOST,
    port=settings.MODBUS_PORT,
    framer=FramerType.SOCKET,
)
client.connect()

def twosComplement_hex(hexval):
    bits = 16
    val = int(hexval, bits)
    if val & (1 << (bits-1)):
        val -= 1 << bits
    return val

def Consulta_Inversor():
    Cadena1 = client.read_holding_registers(4, count=8, slave= int(os.environ['Variador']))
    Cadena2 = client.read_holding_registers(13, count=1, slave= int(os.environ['Variador']))

    frecuencia_ref = float(twosComplement_hex(hex(Cadena1.registers[0]))) / 100
    intensidad = float(twosComplement_hex(hex(Cadena1.registers[4])))
    frecuencia = float(twosComplement_hex(hex(Cadena1.registers[5]))) / 100
    tension = float(twosComplement_hex(hex(Cadena1.registers[6])))
    dc_bus = float(twosComplement_hex(hex(Cadena1.registers[7])))
    estado = int(twosComplement_hex(hex(Cadena2.registers[0])))
    valores = {'frecuencia_ref': frecuencia_ref, 'estado': estado, 'intensidad': intensidad, 
               'frecuencia': frecuencia, 'tension': tension, 'dc_bus': dc_bus }
    return(valores)

def Consulta_Inversor_Avanzada():
    Cadena1 = client.read_holding_registers(0, count=2, slave= int(os.environ['Variador']))
    Cadena2 = client.read_holding_registers(6, count=2, slave= int(os.environ['Variador']))
    
    potencia_variador = twosComplement_hex(hex(Cadena1.registers[0]))
    input_voltaje = twosComplement_hex(hex(Cadena1.registers[1]))
    acceleration_time = float(twosComplement_hex(hex(Cadena2.registers[0]))) / 10
    desacceleration_time = float(twosComplement_hex(hex(Cadena2.registers[0]))) / 10

    valores = {'potencia_variador': potencia_variador, 'input_voltaje': input_voltaje, 'acceleration_time': acceleration_time, 
               'desacceleration_time': desacceleration_time}
    
    with open('app/data/configuracion_variador.json', 'w') as fp:
        json.dump(valores, fp)

def Escribir_variador(valores):
    estado = valores['estado']
    frecuencia_ref = valores['frecuencia'] * 100

    ## Modificar Frecuencia referencia
    client.write_register(4352, frecuencia_ref, slave= int(os.environ['Variador']))

    ## Modificar Estado Variador
    if estado == True:
        client.write_register(5, 194, slave= int(os.environ['Variador']))
    else:
        client.write_register(5, 193, slave= int(os.environ['Variador']))