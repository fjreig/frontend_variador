from fasthtml import FastHTML
from pathlib import Path
from fasthtml.common import *
from fh_altair import altair_headers
from monsterui.all import *
import pandas as pd
from typing import Optional

from app.table import pagina_final
from app.models import (
    get_df,
    get_info_value,
    new_register
)
from app.modbus import Consulta_Inversor, Escribir_variador, Consulta_Inversor_Avanzada
from app.src import Obtener_todos_equipos
from app.dashboard import (
    generate_chart_Intensidades,
    generate_chart_Tensiones,
    generate_chart_Frecuencias,
    Generar_Cards
)

from app.control import (
    Info_Control_variador, 
    Info_Avanzada_Variador, 
    Info_Alarmas_Variador1,
    Info_Alarmas_Variador2,
    Info_Actual_Variador,
    Info_Estado
)

hdrs = (MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), altair_headers, Theme.blue.headers())
app, rt = fast_app(hdrs=hdrs)

@dataclass
class Busqueda:
    Elemento_Buscar: str

@dataclass
class Control_variador:
    estado: Optional[bool] = None
    frecuencia: Optional[int] = None

@rt('/')
def tabla():
    valores = Obtener_todos_equipos()
    return(pagina_final(valores))

@rt('/control')
def index():
    try:
        valores = get_info_value()
        return Title("Control del variador"),Container(
            H2('Control'),
            DivRAligned(
                Button("Graficas", cls=ButtonT.primary, hx_post="/graficas",),
                Button("Volver", cls=ButtonT.destructive, hx_post="/return",),
            ),
            Grid(
            *map(Div,(
                        Div(Info_Control_variador(),Info_Estado(valores), cls='space-y-4'),
                        Div(Info_Avanzada_Variador(), Info_Alarmas_Variador1(valores), cls='space-y-4'),
                        Div(Info_Actual_Variador(valores), Info_Alarmas_Variador2(valores), cls='space-y-4'),
                        )
                ),
            cols_md=1, cols_lg=2, cols_xl=3))
    except:
        return Title("Control del variador"),Container(
            H2('Control'),
            DivRAligned(
                Button("Graficas", cls=ButtonT.primary, hx_post="/graficas",),
                Button("Volver", cls=ButtonT.destructive, hx_post="/return",),
            ),
        )
    
@rt("/Grafico")
def graficos():
    try:
        df_variador = get_df()
        return Title("Dashboard Power Electronics"), Container(
            H2('Graficos'),
            DivRAligned(
                    Button("Refrescar", cls=ButtonT.primary, hx_post="/graficas",),
                    Button("Control", cls=ButtonT.primary, hx_post="/control_vari",),
                    Button("Volver", cls=ButtonT.destructive, hx_post="/return",),
                ),
            Generar_Cards(df_variador),
            Grid(
                Card(Safe(generate_chart_Intensidades(df_variador)), cls='col-span-2'),
                Card(Safe(generate_chart_Tensiones(df_variador)), cls='col-span-2'),
                Card(Safe(generate_chart_Frecuencias(df_variador)), cls='col-span-3'),
                gap=2,cols_xl=7,cols_lg=7,cols_md=1,cols_sm=1,cols_xs=1),
            cls=('space-y-4', ContainerT.xl)
            )
    except:
        return Title("Dashboard Power Electronics"), Container(
            H2('Graficos'),
            DivRAligned(
                    Button("Refrescar", cls=ButtonT.primary, hx_post="/graficas",),
                    Button("Control", cls=ButtonT.primary, hx_post="/control_vari",),
                    Button("Volver", cls=ButtonT.destructive, hx_post="/return",),
                ),
            cls=('space-y-4', ContainerT.xl)
            )

@rt("/update")
def post():
    valores_emi = Consulta_Inversor()
    new_register(valores_emi)
    return Redirect(f"/")

@rt("/control_variador")
def post(valor: Control_variador):
    valor = valor.__dict__
    Escribir_variador(valor)
    Consulta_Inversor_Avanzada()
    return Redirect(f"/")

@app.post("/return")
def post():
    return Redirect(f"/")

@app.post("/control_vari")
def post():
    return Redirect(f"/control")

@app.post("/graficas")
def post():
    return Redirect(f"/Grafico")

serve()