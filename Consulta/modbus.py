import pymodbus.client as ModbusClient
from pymodbus import  FramerType, ModbusException, pymodbus_apply_logging_config
import os

from helper import (
    Decoder_Variador,
)

client: ModbusClient.ModbusBaseSyncClient
client = ModbusClient.ModbusTcpClient(
    os.environ['MODBUS_host'],
    port= os.environ['MODBUS_port'],
    framer=FramerType.SOCKET,
)
client.connect()

def Consulta_Variador():
    Cadena1 = client.read_holding_registers(4, count=8, slave= int(os.environ['Variador']))
    Cadena2 = client.read_holding_registers(13, count=1, slave= int(os.environ['Variador']))
    valores = Decoder_Variador(Cadena1, Cadena2) 
    return(valores)