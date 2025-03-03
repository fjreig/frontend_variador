import pandas as pd

from app.models import get_last_value

def Obtener_todos_equipos():
    Error_Variador = False
    try:
        df1 = pd.DataFrame(get_last_value())
    except:
        df1 = pd.DataFrame()
        Error_Variador = True

    valores = df1.to_dict('records')
    return(valores)