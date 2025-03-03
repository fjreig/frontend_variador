import pymodbus.client as ModbusClient
from pymodbus import  FramerType, ModbusException, pymodbus_apply_logging_config
import datetime
import os

client: ModbusClient.ModbusBaseSyncClient
client = ModbusClient.ModbusTcpClient(
    os.environ['MODBUS_host'],
    port= os.environ['MODBUS_port'],
    framer=FramerType.SOCKET,
)
client.connect()

def twosComplement_hex(hexval):
    bits = 16
    val = int(hexval, bits)
    if val & (1 << (bits-1)):
        val -= 1 << bits
    return val

def Consulta_Variador(Cadena1, Cadena2, Cadena3):
    Cadena1 = client.read_holding_registers(4, count=8, slave= int(os.environ['Variador']))
    Cadena2 = client.read_holding_registers(13, count=1, slave= int(os.environ['Variador']))
    Cadena3 = client.read_holding_registers(815, count=2, slave= int(os.environ['Variador']))

    frecuencia_ref = float(twosComplement_hex(hex(Cadena1.registers[0]))) / 100
    intensidad = float(twosComplement_hex(hex(Cadena1.registers[4])))
    frecuencia = float(twosComplement_hex(hex(Cadena1.registers[5]))) / 100
    tension = float(twosComplement_hex(hex(Cadena1.registers[6])))
    dc_bus = float(twosComplement_hex(hex(Cadena1.registers[7])))
    estado = int(twosComplement_hex(hex(Cadena2.registers[0])))
    trip1 = twosComplement_hex(hex(Cadena3.registers[0]))
    trip2 = twosComplement_hex(hex(Cadena3.registers[1]))
    
    valores = {'fecha' : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'frecuencia_ref': frecuencia_ref,
        'estado': estado, 'intensidad': intensidad, 'frecuencia': frecuencia, 'tension': tension,
        'dc_bus': dc_bus, 'trip1': trip1, 'trip2': trip2 }
    return(valores)