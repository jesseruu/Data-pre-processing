import pandas as pd 

dataE = pd.read_excel("homicidios_2020_0.xls")

def convert(self):
    self.to_csv("homicidios_2020_.csv")
    return pd.read_csv("homicidios_2020_.csv")

dataC = convert(dataE)

IndexMunicipios = dataC[dataC['MUNICIPIO'] != 'BOGOTÁ D.C. (CT)'].index
dataC.drop(IndexMunicipios, inplace = True)
dataC.drop(['Unnamed: 0', 'DEPARTAMENTO', 'CODIGO DANE', 'FECHA HECHO'], axis = 1, inplace = True)

dataC = pd.get_dummies(dataC, columns=['GENERO'], drop_first=True)
dataC.rename(columns={'GENERO_MASCULINO':'GENERO'}, inplace = True)
dataC['ARMAS MEDIOS'] = pd.Categorical(dataC['ARMAS MEDIOS'], categories=['ARMA DE FUEGO','ARMA BLANCA / CORTOPUNZANTE','CONTUNDENTES'])
dataC['AGRUPA EDAD PERSONA'] = pd.Categorical(dataC['AGRUPA EDAD PERSONA'], categories=['ADULTOS','ADOLESCENTES','MENORES'])

codes, uniques = pd.factorize(dataC['ARMAS MEDIOS'])
codesTwo, uniquesTwo = pd.factorize(dataC['AGRUPA EDAD PERSONA'])

dataC['ARMAS MEDIOS'] = codes
dataC['AGRUPA EDAD PERSONA'] = codesTwo


print(dataC.head(15))

