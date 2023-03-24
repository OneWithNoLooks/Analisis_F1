import urllib.request, json
#Resultados de carreras F1 Temporada 2022

def getDatos():
    print("Buscando Archivo...")
    try:
        with open("./datos.txt", "r") as f:
            print("Archivo encontrado")
            data = json.load(f)    
        return(data['MRData'])
    
    except Exception:
        print("Error buscando el archivo")
        print("Creando dataset...") 
        with urllib.request.urlopen("http://ergast.com/api/f1/2022/results.json?limit=500") as rawdata:
            data = json.load(rawdata)
        with open('./datos.txt', 'w') as f:
            json.dump(data, f)
            print('Archivo creado con exito')
        return(data['MRData'])
        
        