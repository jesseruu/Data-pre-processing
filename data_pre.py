import pandas as pd 
from time import sleep
import os

def limpia_terminal(operatingSystem):
    if operatingSystem == 'nt':
        return os.system("cls")
    else:
        return os.system("clear")

def convertir_formato():
    dataE = pd.read_excel("homicidios_2020_0.xls")
    dataE.to_csv("homicidios_2020_.csv")
    return pd.read_csv("homicidios_2020_.csv")

def preparar_data(data):
    print("\t\t Filtrando datos....")
    sleep(1)
    IndexMunicipios = data[data['MUNICIPIO'] != 'BOGOTÁ D.C. (CT)'].index
    data.drop(IndexMunicipios, inplace = True)
    print("\t\t Eliminando columnas innecesarias....")
    sleep(1)
    data.drop(['Unnamed: 0', 'DEPARTAMENTO', 'CODIGO DANE', 'FECHA HECHO'], axis = 1, inplace = True)

    limpia_terminal(os.name)
    print("\t\t ¡Dataset limpio!")

def categorizar_data(data):
    data['GENERO'] = pd.Categorical(data['GENERO'], categories=['MASCULINO','FEMENINO'])
    data['ARMAS MEDIOS'] = pd.Categorical(data['ARMAS MEDIOS'], categories=['ARMA DE FUEGO','ARMA BLANCA / CORTOPUNZANTE','CONTUNDENTES'])
    data['AGRUPA EDAD PERSONA'] = pd.Categorical(data['AGRUPA EDAD PERSONA'], categories=['ADULTOS','ADOLESCENTES','MENORES'])

    return data['GENERO'], data['ARMAS MEDIOS'], data['AGRUPA EDAD PERSONA']

def factoriza_data(data):
    genero, arma, edad = categorizar_data(data)
    codesg, uniquesg = pd.factorize(genero)
    codesa, uniquesa = pd.factorize(arma)
    codese, uniquese = pd.factorize(edad)
    
    print("\t\t Categorizando columnas....")
    sleep(1)

    data['GENERO'] = codesg
    data['ARMAS MEDIOS'] = codesa
    data['AGRUPA EDAD PERSONA'] = codese

    print("\t\t Asignando valores numericos....")
    sleep(1)

    limpia_terminal(os.name)
    
    print("\n\t\t\tTABLA DE CATEGORIZACION")
    print("\n\t",uniquesg[0],"   |", uniquesa[0],"|",uniquese[0], "      = 0")
    print("\t", uniquesg[1],"    |", uniquesa[1],"\t\t    |",uniquese[1], " = 1")
    print("\t", uniquesa[2],"|", uniquese[2], " \t\t\t\t    = 2")
    print("\n\t\t\t ¡Categorizacion completa!")


def exportar_data(data):
    nombre = input("\t\t Digite el nombre del nuevo archivo csv: ")
    nombre += ".csv"
    print("\t\t Guardando nuevo archivo csv....")
    data.to_csv(nombre, index = False)
    limpia_terminal(os.name)
    print("\t\t ¡Guardado completo!")

def main():

    option = 0
    dataC = convertir_formato()
    limpia_terminal(os.name)

    while option != '4':
        print("\t\t==========================================")
        print("\n\t\t PRE-PROCESAMIENTO DE DATOS CON PYTHON")
        print("\n\t\t 1. Limpiar datos")
        print("\t\t 2. Categorizar datos")
        print("\t\t 3. Importar dataset a un nuevo csv")
        print("\t\t 4. Salir")
        option = input("\n\t\t Digite el numero de la opcion: ")
        print("\t\t==========================================")
 
        if option == '1':
            preparar_data(dataC)
            
        elif option == '2':
            categorizar_data(dataC)
            factoriza_data(dataC)

        elif option == '3':
            exportar_data(dataC)

        elif option == '4':
            os.remove("homicidios_2020_.csv")
            print("\t\t Cerrando...")
            sleep(1)

        else:
            print("\t\t Digite una opcion valida")
            limpia_terminal(os.name)
        
if __name__ == "__main__":
    main()


