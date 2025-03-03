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
    new_register
)
from app.modbus import Consulta_Inversor, Escribir_variador
from app.src import Obtener_todos_equipos
from app.dashboard import (
    generate_chart_Intensidades,
    generate_chart_Tensiones,
    generate_chart_Frecuencias,
    Generar_Cards
)

from app.control import Control_Variador

hdrs = (MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), altair_headers, Theme.green.headers())
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
    return Title("Control del variador"),Container(
            DivRAligned(
                Button("Graficas", cls=ButtonT.primary, hx_post="/graficas",),
                Button("Refrescar", cls=ButtonT.primary, hx_post="/graficas",),
                Button("Volver", cls=ButtonT.destructive, hx_post="/return",),
            ),
            Grid(
            *map(Div,(
                      Div(Control_Variador, cls='space-y-4'),
                      )
                ),
         cols_md=1, cols_lg=2, cols_xl=3))

@rt("/Grafico")
def graficos():
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

@rt("/update")
def post():
    valores_emi = Consulta_Inversor()
    new_register(valores_emi)
    return Redirect(f"/")

@rt("/control_variador")
def post(valor: Control_variador):
    valor = valor.__dict__
    Escribir_variador(valor)
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