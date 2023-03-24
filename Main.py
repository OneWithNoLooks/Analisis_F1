#
from API import getDatos
from Limpieza import limpieza
from Tabulacion import tabularExcel

def AnalisisF1():
    datos = dict()
    datos = getDatos()
    lista_carreras = limpieza(datos)
    tabularExcel(lista_carreras)


if __name__ == "__main__":
    AnalisisF1()



    
