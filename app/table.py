from fasthtml.common import *
from monsterui.all import *

header_data = ['Variable', 'Valor', 'Unidades', 'Fecha_Actualizacion']

def definir_tabla(tabla_id, Titulo_tabla):
    tabla_def = Section(
        H2(Titulo_tabla),
        tabla_id,
        cls="my-6")
    return(tabla_def)

def table_valores(body_data):
    return definir_tabla(TableFromDicts(header_data, body_data, 
        header_cell_render=lambda v: Th(v.upper())), "Tabla de Valores")

def pagina_final(valores):
    return Title("Modbus Desk Dashboard"), Container(
            DivFullySpaced(
                H2("Monitorizacion Power Electronics"),
                DivRAligned(
                    Button(UkIcon("plus-circle", cls="mr-2"), "Actualizar", cls=ButtonT.primary, hx_post="/update"),
                    Button("Graficas", cls=ButtonT.primary, hx_post="/graficas",),
                    Button("Control", cls=ButtonT.destructive, hx_post="/control_vari"),
                ),
                cls='mb-8'),
            table_valores(valores),
            Loading(htmx_indicator=True, type=LoadingT.dots, cls="fixed top-0 right-0 m-4"),
            cls="mx-auto max-w-7xl"
        )