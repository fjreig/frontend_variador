import datetime

from modbus import(
    Consulta_Variador,
)

from models import (
    new_register_variador
)

def main():
    Error_Variador_Comunicacion = False
    x = datetime.datetime.now()
    print(x)

    try:
        valores_inversor1 = Consulta_Variador()
        new_register_variador(valores_inversor1)
    except:
        Error_Variador_Comunicacion = True
        print(Error_Variador_Comunicacion)
 
if __name__ == "__main__":
    main()