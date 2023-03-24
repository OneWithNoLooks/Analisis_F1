# ['season', 'round', 'url', 'raceName', 'Circuit', 'date', 'time', 'Results']
# Los datos no incluyen VueltasRapidas, REVISAR ESO!!!

def limpieza(datosraw):
    lista_carreras = list()
    for ronda in datosraw['RaceTable']['Races']:        
        r = {'Ronda':ronda['round'], 'Circuito':ronda['Circuit']['circuitName'], 'NombreGP':ronda['raceName'], 'Fecha':ronda['date'],
             'Resultado':ronda['Results']}
        lista_carreras.append(r)
    
    for race in lista_carreras:
        temp = list()
        piloto = dict()
        resultados = race['Resultado']
        race.pop('Resultado')
        for resultado in resultados:
            if resultado['status'] == 'Finished':
                piloto = {'numeroPiloto':resultado['number'], 
                          'posicionFinal':resultado['position'],
                          'puntosObtenidos':resultado['points'], 
                          'piloto':resultado['Driver']['givenName']+' '+resultado['Driver']['familyName'],
                          'constructor':resultado['Constructor']['name'],
                          'posicionInicial':resultado['grid'], 
                          'estado':resultado['status'], 
                          'tiempo':resultado['Time']['time'], 
                        }
                temp.append(piloto)
            else:
                piloto = {'numeroPiloto':resultado['number'], 
                          'posicionFinal':resultado['position'],
                          'puntosObtenidos':resultado['points'], 
                          'piloto':resultado['Driver']['givenName']+resultado['Driver']['familyName'],
                          'constructor':resultado['Constructor']['name'],
                          'posicionInicial':resultado['grid'], 
                          'estado':resultado['status'], 
                        }
                temp.append(piloto)
            piloto = dict()
        race['Resultado'] = temp
    
    return lista_carreras
        
        
        
    