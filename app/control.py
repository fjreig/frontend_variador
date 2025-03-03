from fasthtml.common import *
from fasthtml.components import Uk_input_tag
from fasthtml.svg import *
from monsterui.all import *

Control_Variador = Card(
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