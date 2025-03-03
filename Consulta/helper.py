import codecs
import struct
import datetime
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

import codecs
import struct

def convertir(valor1, valor2):
    if len(valor1) % 2 == 0:
        valor1 = str(valor1)
    else:
        valor1 = "0" + str(valor1)
    if len(valor2) % 2 == 0:
        valor2 = str(valor2)
    else:
        valor2 = "0" + str(valor2)
    valor3 = valor1 + valor2
    valor3 = int(valor3,16)
    return(valor3)

def convertirUNSIGNED(valor1, valor2):
    for i in range(4):
        if len(valor1) < 4:
            valor1 = "0" + valor1
    for i in range(4):
        if len(valor2) < 4:
            valor2 = "0" + valor2
    valor = valor1 + valor2
    valor = codecs.decode(valor, 'hex')
    valor = round(struct.unpack('>l', valor)[0],2)
    return (valor)

def twosComplement_hex(hexval):
    bits = 16
    val = int(hexval, bits)
    if val & (1 << (bits-1)):
        val -= 1 << bits
    return val

def Decoder_Variador(Cadena1, Cadena2):
    frecuencia_ref = float(twosComplement_hex(hex(Cadena1.registers[0]))) / 100
    intensidad = float(twosComplement_hex(hex(Cadena1.registers[4])))
    frecuencia = float(twosComplement_hex(hex(Cadena1.registers[5]))) / 100
    tension = float(twosComplement_hex(hex(Cadena1.registers[6])))
    dc_bus = float(twosComplement_hex(hex(Cadena1.registers[7])))
    estado = int(twosComplement_hex(hex(Cadena2.registers[0])))
    valores = {'fecha' : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'frecuencia_ref': frecuencia_ref,
        'estado': estado, 'intensidad': intensidad, 'frecuencia': frecuencia, 'tension': tension,
        'dc_bus': dc_bus }
    return(valores)