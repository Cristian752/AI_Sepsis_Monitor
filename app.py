# Dashboard Sepsis
# Cristian Toro

#---------------------------------------------------------------------------------------------------------#
# 0. Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

#---------------------------------------------------------------------------------------------------------#

# 1. DataPacientes llamado del dataset
csv_path = 'assets/TrainCompletoOrdenado.csv'
DataPacientes = pd.read_csv(csv_path, sep=',')


# 2. Formats and templates
external_stylesheets = ['https://codepen.io/chriddyo/pen/bWLwgP.css']
tickFont = {'size':9, 'color':'rgb(30,30,30)'}


# 3. Generar la lista de pacientes
pacientes = DataPacientes['Paciente'].unique()
pacientes.sort()
options = [{'label': i, 'value': i} for i in pacientes]

#---------------------------------------------------------------------------------------------------------#

# 4. Dashboard layout
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Sepsis Dashboard'


app.layout = html.Div([
    
    
    #Header
    html.Div([
        html.H1(' AI Sepsis Monitor'),
        html.Img(src='assets/imagen1.png')
    ], className= 'banner'),

     html.Div(
                [
                    html.H1("Control de pacientes hospitalizados", style={'textAlign': 'center'}),
                    html.P("Este monitor te brinda la información necesaria de cada paciente", style={'textAlign': 'center'}),
                ],
                className='container header'
            ),

    #Despliegue de la lista de pacientes
    html.Div([ 
             html.Div([
                      html.P('Seleccione el paciente', className = 'fix_label', 
                              style = {'color':'black', 'margin-top': '2px'}),
                      dcc.Dropdown( id = 'paciente-picker',
                                    options = options,
                                    value = 'p000009'),
             ], className='creatw_container2 five columns', style={'width':'40%'}),                    
    ], className='row flex-display'),
    
    #Espacio en blanco investigar como hacer el salto de linea
    html.Div([
         html.P('', className = 'fix_label', 
                              style = {'color':'black', 'margin-top': '2px'})
    ]),
  

    #Tabs
    html.Div([
    dcc.Tabs(
        id="tabs-with-classes",
        value='tab-1',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Datos vitales',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Datos de laboratorio',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Demograficos',
                value='tab-3', className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Predicción',
                value='tab-4',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
        ]),
    html.Div(id='tabs-content-classes')
    ]),
    
]) #end layout

#---------------------------------------------------------------------------------------------------------#

# 5. Callback (Input and Output) y Def
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 5.1. (DEF and CALLBACK) DATOS VITALES

# HR
@app.callback(
              Output(component_id='scatterHR_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(scatterHR_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == scatterHR_graph]
    fig = px.scatter(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'HR')
    fig.update_traces(mode='lines+markers')
    fig.update_xaxes(showgrid=False)
    fig.update_layout(
        title= 'HR para el paciente {}'.format(scatterHR_graph))

    return fig

# O2Sat
@app.callback(
              Output(component_id='scatterO2Sat_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(scatterO2Sat_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == scatterO2Sat_graph]
    fig2 = px.scatter(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'O2Sat')
    fig2.update_traces(mode='lines+markers')
    fig2.update_xaxes(showgrid=False)
    fig2.update_layout(
        title= 'O2Sat para el paciente {}'.format(scatterO2Sat_graph))

    return fig2

# Temp
@app.callback(
              Output(component_id='barTemp_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(barTemp_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == barTemp_graph]
    fig3 = px.bar(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'Temp')
    fig3.update_layout(
        title= 'Temp para el paciente {}'.format(barTemp_graph))

    return fig3

# Map
@app.callback(
              Output(component_id='barMap_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(barMap_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == barMap_graph]
    fig4 = px.bar(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'MAP')
    fig4.update_layout(
        title= 'MAP para el paciente {}'.format(barMap_graph))
    
    return fig4

# SBP
@app.callback(
              Output(component_id='scatterSBP_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(scatterSBP_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == scatterSBP_graph]
    fig5 = px.scatter(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'SBP')
    fig5.update_traces(mode='lines+markers')
    fig5.update_xaxes(showgrid=False)
    fig5.update_layout(
        title= 'SBP para el paciente {}'.format(scatterSBP_graph))

    return fig5

# DBP
@app.callback(
              Output(component_id='scatterDBP_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(scatterDBP_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == scatterDBP_graph]
    fig6 = px.scatter(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'DBP')
    fig6.update_traces(mode='lines+markers')
    fig6.update_xaxes(showgrid=False)
    fig6.update_layout(
        title= 'DBP para el paciente {}'.format(scatterDBP_graph))

    return fig6

# Resp
@app.callback(
              Output(component_id='scatterResp_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(scatterResp_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == scatterResp_graph]
    fig7 = px.scatter(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'Resp')
    fig7.update_traces(mode='lines+markers')
    fig7.update_xaxes(showgrid=False)
    fig7.update_layout(
        title= 'Resp para el paciente {}'.format(scatterResp_graph))

    return fig7

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 5.2 (DEF and CALLBACK) DATOS DE LABORATORIO

# WBC
@app.callback(
              Output(component_id='scatterWBC_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(scatterWBC_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == scatterWBC_graph]
    fig8 = px.scatter(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'WBC')
    fig8.update_traces(mode='lines+markers')
    fig8.update_xaxes(showgrid=False)
    fig8.update_layout(
        title= 'WBC para el paciente {}'.format(scatterWBC_graph))

    return fig8

# Bilirubin_total
@app.callback(
              Output(component_id='scatterBT_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(scatterBT_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == scatterBT_graph]
    fig9 = px.scatter(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'Bilirubin_total')
    fig9.update_traces(mode='lines+markers')
    fig9.update_xaxes(showgrid=False)
    fig9.update_layout(
        title= 'Bilirubin_total para el paciente {}'.format(scatterBT_graph))

    return fig9

# FiO2
@app.callback(
              Output(component_id='barFiO2_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(barFiO2_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == barFiO2_graph]
    fig10 = px.bar(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'FiO2')
    fig10.update_layout(
        title= 'FiO2 para el paciente {}'.format(barFiO2_graph))

    return fig10

# BUN
@app.callback(
              Output(component_id='barBUN_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(barBUN_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == barBUN_graph]
    fig11 = px.bar(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'BUN')
    fig11.update_layout(
        title= 'BUN para el paciente {}'.format(barBUN_graph))
    
    return fig11




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 5.3 (DEF and CALLBACK) DATOS DE DEMOGRAFICOS



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 5.4 (DEF and CALLBACK) DATOS DE PREDICCIÓN

# SepsisLabel
@app.callback(
              Output(component_id='scatterSL_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(scatterSL_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == scatterSL_graph]
    fig12 = px.scatter(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'SepsisLabel')
    fig12.update_traces(mode='lines+markers')
    fig12.update_xaxes(showgrid=False)
    fig12.update_layout(
        title= 'SepsisLabel para el paciente {}'.format(scatterSL_graph))

    return fig12

# Prediccion
@app.callback(
              Output(component_id='scatterPred_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(scatterPred_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == scatterPred_graph]
    fig13 = px.scatter(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'Prediccion')
    fig13.update_traces(mode='lines+markers')
    fig13.update_xaxes(showgrid=False)
    fig13.update_layout(
        title= 'Prediccion para el paciente {}'.format(scatterPred_graph))

    return fig13

# Sepsis_SIRS
@app.callback(
              Output(component_id='barSSirs_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(barSSirs_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == barSSirs_graph]
    fig14 = px.bar(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'Sepsis_SIRS')
    fig14.update_layout(
        title= 'Sepsis_SIRS para el paciente {}'.format(barSSirs_graph))

    return fig14

# Sepsis_SOFA
@app.callback(
              Output(component_id='barSSofa_graph', component_property= 'figure'),
             [Input(component_id= 'paciente-picker', component_property = 'value')])

def update_bar_chart(barSSofa_graph):

    filtered_df = DataPacientes[DataPacientes['Paciente'] == barSSofa_graph]
    fig15 = px.bar(
                 data_frame = filtered_df,
                 x = 'ICULOS',
                 y = 'Sepsis_SOFA')
    fig15.update_layout(
        title= 'Sepsis_SOFA para el paciente {}'.format(barSSofa_graph))
    
    return fig15




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 5.5 (DEF and CALLBACK) TABS

@app.callback(Output('tabs-content-classes', 'children'),
              Input('tabs-with-classes', 'value'))

def render_content(tab):

    if tab == 'tab-1':
        
        return html.Div([
                         html.Div([
                                html.H3('Datos vitales', style={'textAlign': 'center'}),
                         ], className= 'banner'),

                         html.Div([
                                   html.Center(
                                   html.P(["En este espacio se encuentran los datos vitales del paciente seleccionado "]),
                                   ),
                         ], className='container footer preprint'),
                         
                         html.Div([   
                                    html.Div([
                                             
                                              html.Div([
                                              html.P([
                                              html.B("Frecuencia cardíaca")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                             dcc.Graph(id = 'scatterHR_graph', figure ={})
                                    ], className = 'create_container2 eight columns'),

                                    html.Div([

                                              html.Div([
                                              html.P([
                                              html.B("Nivel de oxigeno en la sangre")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'scatterO2Sat_graph', figure ={})
                                            ], className = 'create_container2 eight columns'),
                         ],className = 'row flex-display'),


                         html.Div([
                                   html.Div([

                                            html.Div([
                                            html.P([
                                            html.B("Temperatura")],style={'textAlign': 'center'}),
                                   ],className='container footer permalink'),

                                            dcc.Graph(id = 'barTemp_graph', figure ={})
                                   ], className = 'create_container2 eight columns'),

                                   html.Div([

                                            html.Div([
                                              html.P([
                                              html.B("Presión arterial media")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'barMap_graph', figure ={})
                                   ], className = 'create_container2 eight columns'),
                        
                         ],className = 'row flex-display'),


                        html.Div([
                                   html.Div([

                                            html.Div([
                                              html.P([
                                              html.B("Presión arterial sistolica")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'scatterSBP_graph', figure ={})
                                   ], className = 'create_container2 eight columns'),

                                    html.Div([

                                            html.Div([
                                              html.P([
                                              html.B("Presión arterial diastolica")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'scatterDBP_graph', figure ={})
                                    ], className = 'create_container2 eight columns'),
                        
                         ],className = 'row flex-display'),


                        html.Div([
                                   html.Div([

                                            html.Div([
                                              html.P([
                                              html.B("Respiración")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'scatterResp_graph', figure ={})
                                   ], className = 'create_container2 eight columns'),
                        
                         ],className = 'row flex-display'),
                         
        ])   
  

    elif tab == 'tab-2':
        
        return html.Div([
                         html.Div([
                                html.H3('Datos de laboratorio', style={'textAlign': 'center'}),
                         ], className= 'banner'),

                         html.Div([
                                   html.Center(
                                   html.P(["En este espacio se encuentran los datos de laboratorio del paciente seleccionado "]),
                                   ),
                         ], className='container footer preprint'),
                         
                         html.Div([
                                    html.Div([

                                              html.Div([
                                              html.P([
                                              html.B("Leucocitos")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                             dcc.Graph(id = 'scatterWBC_graph', figure ={})
                                    ], className = 'create_container2 eight columns'),

                                    html.Div([
                                            
                                             html.Div([
                                              html.P([
                                              html.B("Bilirrubina Total")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'scatterBT_graph', figure ={})
                                            ], className = 'create_container2 eight columns'),
                         ],className = 'row flex-display'),


                         html.Div([
                                   html.Div([

                                             html.Div([
                                              html.P([
                                              html.B("Fracción inspirada de oxigeno")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'barFiO2_graph', figure ={})
                                   ], className = 'create_container2 eight columns'),

                                   html.Div([

                                             html.Div([
                                              html.P([
                                              html.B("Nitrogeno ureico en sangre")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'barBUN_graph', figure ={})
                                   ], className = 'create_container2 eight columns'),
                        
                         ],className = 'row flex-display'),
        ]) 

    elif tab == 'tab-3':
       
               return html.Div([
                         html.Div([
                                html.H3('Datos demograficos', style={'textAlign': 'center'}),
                         ], className= 'banner'),

                        html.Div([
                                   html.Center(
                                   html.P(["En este espacio se encuentran los datos demograficos del paciente seleccionado "]),
                                   ),
                         ], className='container footer preprint'),

                        html.Div([
                                    html.Div([
                                            dcc.Graph(id = 'scatter1_graph', figure ={})
                                    ], className = 'create_container2 eight columns'),

                                    html.Div([
                                            dcc.Graph(id = 'scatter2_graph', figure ={})
                                    ], className = 'create_container2 eight columns')
                        ], className = 'row flex-display')   
        ])

    elif tab == 'tab-4':
        
        return html.Div([
                         html.Div([
                                html.H3('Predicciones', style={'textAlign': 'center'}),
                         ], className= 'banner'),

                        html.Div([
                                   html.Center(
                                   html.P(["En este espacio se encuentran los datos de predicción del paciente seleccionado "]),
                                   ),
                         ], className='container footer preprint'),
                         
                         html.Div([
                                    html.Div([
                                             html.Div([
                                              html.P([
                                              html.B("Sepsis Label")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                             dcc.Graph(id = 'scatterSL_graph', figure ={})
                                    ], className = 'create_container2 eight columns'),

                                    html.Div([
                                            html.Div([
                                              html.P([
                                              html.B("Predicción de sepsis")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'scatterPred_graph', figure ={})
                                            ], className = 'create_container2 eight columns'),
                         ],className = 'row flex-display'),


                         html.Div([
                                   html.Div([
                                            html.Div([
                                              html.P([
                                              html.B("Predicción SIRS")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'barSSirs_graph', figure ={})
                                   ], className = 'create_container2 eight columns'),

                                   html.Div([

                                            html.Div([
                                              html.P([
                                              html.B("Predicción SOFA")],style={'textAlign': 'center'}),
                                    ],className='container footer permalink'),

                                            dcc.Graph(id = 'barSSofa_graph', figure ={})
                                   ], className = 'create_container2 eight columns'),
                        
                         ],className = 'row flex-display'),
        ]) 

if __name__ ==('__main__'):
    app.run_server(debug=True)


