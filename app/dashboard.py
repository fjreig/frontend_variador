from fasthtml.common import *
import fasthtml.common as fh
from monsterui.all import *
from fasthtml.svg import *
import plotly.express as px

def generate_chart_Intensidades(df):    
    fig = px.line(df, x='fecha', y=['intensidad'],  template='plotly_white', line_shape='spline')
    fig.update_traces(mode='lines+markers')
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20), hovermode='x unified',
        showlegend=True, legend=dict(orientation='h', yanchor='bottom', y=1.02,  xanchor='right', x=1),
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showline=True, linewidth=1, linecolor='white', gridcolor='rgba(0,0,0,0)'),
        yaxis=dict(showline=True, linewidth=1, linecolor='white', gridcolor='rgba(0,0,0,0)'))
    fig.update_layout(xaxis_title="Fecha", yaxis_title="Intensidad [A]")
    fig.update_yaxes(title_font_color="white", color="white", rangemode="tozero")
    fig.update_xaxes(title_font_color="white", color="white")
    return fig.to_html(include_plotlyjs=True, full_html=False, config={'displayModeBar': False})

def generate_chart_Tensiones(df):    
    fig = px.line(df,x='fecha', y=['tension'],template='plotly_white',line_shape='spline')
    fig.update_traces(mode='lines+markers')
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20), hovermode='x unified',
        showlegend=True, legend=dict(orientation='h', yanchor='bottom', y=1.02,  xanchor='right', x=1),
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0)'),
        yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0)'))
    fig.update_layout(xaxis_title="Fecha", yaxis_title="Tension [V]")
    fig.update_yaxes(title_font_color="white", color="white", rangemode="tozero")
    fig.update_xaxes(title_font_color="white", color="white")
    return fig.to_html(include_plotlyjs=True, full_html=False, config={'displayModeBar': False})

def generate_chart_Frecuencias(df):    
    fig = px.line(df, x='fecha', y=['frecuencia', 'frecuencia_ref'],  template='plotly_white', line_shape='spline')
    fig.update_traces(mode='lines+markers')
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20), hovermode='x unified',
        showlegend=True, legend=dict(orientation='h', yanchor='bottom', y=1.02,  xanchor='right', x=1),
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0)'),
        yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0)'))
    fig.update_layout(xaxis_title="Fecha", yaxis_title="Intensidad [A]")
    fig.update_yaxes(title_font_color="white", color="white", rangemode="tozero")
    fig.update_xaxes(title_font_color="white", color="white")
    return fig.to_html(include_plotlyjs=True, full_html=False, config={'displayModeBar': False})

def InfoCard(title, value, change): 
    return Card(H3(value),P(change, cls=TextPresets.muted_sm), header = H4(title))

def tipo_tarjeta(icono, name, valor1, valor2):
    return Card(
        DivLAligned(
            UkIcon(icono, height=50, width=50),
            Div(H3(name), P(valor1), P(valor2))
            ),
        )

def Generar_Cards(df):
    info_card_data = [tipo_tarjeta('plug-zap', "Estado", df['estado'][0], ""),
                    tipo_tarjeta('orbit', "Frecuencia", "Referencia: " + str(df['frecuencia_ref'][0]) + "Hz", "Real: " + str(df['frecuencia'][0]) + "Hz"),
                    tipo_tarjeta('utility-pole', "Tension", str(round(df['tension'][0])) + " V", ""),
                    tipo_tarjeta('thermometer', "Intensidad", str(df['intensidad'][0]) + ' A', "")]
    return Grid(*info_card_data, cols_sm=1, cols_md=1, cols_lg=2, cols_xl=4)