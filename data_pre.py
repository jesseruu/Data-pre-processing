import pandas as pd 
from time import sleep

def convertir_formato():
    dataE = pd.read_excel("homicidios_2020_0.xls")
    dataE.to_csv("homicidios_2020_.csv")
    return pd.read_csv("homicidios_2020_.csv")

def preparar_data(data):
    IndexMunicipios = data[data['MUNICIPIO'] != 'BOGOTÁ D.C. (CT)'].index
    data.drop(IndexMunicipios, inplace = True)
    data.drop(['Unnamed: 0', 'DEPARTAMENTO', 'CODIGO DANE', 'FECHA HECHO'], axis = 1, inplace = True)

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

    data['GENERO'] = codesg
    data['ARMAS MEDIOS'] = codesa
    data['AGRUPA EDAD PERSONA'] = codese

def exportar_data(data):
    name = input("\t\t Digite el nuevo nombre de la data:")
    name += ".csv"
    data.to_csv(name, index = False)

def main():

    option = 0
    dataC = convertir_formato()
    while option != '4':

        print("\t\t PRE-PROCESAMIENTO DE DATOS CON PYTHON")
        print("\t\t 1. Limpiar datos\n\t\t 'Esta opcion limita el municipio de los datos a solo Bogota\n \t\ty elimina las columnas de datos innecesarios'")
        print("\t\t 2. Categorizar datos \n\t\t 'Esta opcion permite categorizan datos la edad, para que sea posible su analisis'")
        print("\t\t 3. Importar la data en un nuevo csv")
        print("\t\t 4. Salir")
        option = input("Digite el numero de la opcion")
 
        if option == '1':

            if not dataC.empty:
                preparar_data(dataC)
            else:
                print("Convierta los datos a csv")

        elif option == '2':
            categorizar_data(dataC)
            factoriza_data(dataC)

        elif option == '3':
            exportar_data(dataC)

        elif option == '4':
            print("\t\t Cerrando...")
            sleep(1)

        else:
            print("\t\t Digite una opcion valida")
        
if __name__ == "__main__":
    main()


