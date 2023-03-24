import pandas as pd
import numpy as np
from pandas import ExcelWriter

# resultados.keys()
#['numeroPiloto', 'posicionFinal', 'puntosObtenidos', 'piloto', 'constructor', 'posicionInicial', 'estado', 'tiempo']
# def autoColumna(dataframe, escritor, sheet):
#     for column in dataframe:
#         column_width = max(dataframe[column].astype(str).map(len).max(), len(column))
#         col_idx = dataframe.columns.get_loc(column)
#         escritor.sheets[sheet].set_column(col_idx, col_idx, column_width)

def tabularExcel(carreras):
    escritor = ExcelWriter('temporada_2022.xlsx')
    
    for carrera in carreras:
        temp = list()
        circuito = {'ronda':int(carrera['Ronda']),
                    'circuito':carrera['Circuito'],
                    'GP':carrera['NombreGP'],
                    'fecha':carrera['Fecha']}
        resultados = carrera['Resultado']

        results = pd.DataFrame(resultados, index=range(0, len(resultados)))
        trackinfo = pd.DataFrame(circuito, index=['Fila '+carrera['Ronda']])

        trackinfo.to_excel(escritor, sheet_name='Ronda '+carrera['Ronda'], index=False, startcol=0)
        results.to_excel(escritor, sheet_name='Ronda '+carrera['Ronda'], index=False, startcol=5)

    escritor.close()
    

