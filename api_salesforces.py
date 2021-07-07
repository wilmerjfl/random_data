from salesforce_api import Salesforce ## pip install salesforce_api
import json
import pandas as pd
import config as pw

client = Salesforce(
    username = pw.username,
    password = pw.password,
    security_token=pw.security_token)### Mediante la api, la funcion Salesforce hace el login a la plataforma salesforce.


clientes = client.sobjects.query("SELECT Name, nombre__c, Apellido__c, Estado__c, Sexo__c, zona_participante__c, Categor_a_c__c, Oficios_Principales_1__c, Oficios_Principales_2__c, Oficios_Principales_3__c FROM participante__c")
## Crea el objeto Clientes con consulta SQL realizada al objeto Participante creado en SalesForce, utilizado la API de salesforce.

datos_json = json.dumps(clientes) ## Transforma os datos

df = pd.read_json(datos_json)# Transforma los datos obetindos en un DataFrame para poder trabajar.

df = df.drop(['attributes'], axis = 1) #Elimino la primera columna de atributos que no se va utilizar.

lista = list(df.head()) #Creo la lista de elementos del atributo zona_participante__c

for i in lista:
    print(i)

atributo = input('Por favor seleccione el campo a filtrar: ')

filtro = set(list(df[atributo]))

for j in filtro:
    print(j)

filtro = input(str("Por favor ingresar que valor desea filtrar: ")) #Consulta porque zona va filtrar el Dataframe.

df = df[df[atributo] == filtro]

df = df.drop(['Estado__c'],axis = 1)
df = df.drop(['Sexo__c'],axis = 1)
df = df.drop(['Categor_a_c__c'],axis = 1)
df = df.drop(['Oficios_Principales_2__c'],axis = 1)
df = df.drop(['Oficios_Principales_3__c'],axis = 1)
df = df.drop(['zona_participante__c'],axis = 1)
df = df.drop(['Oficios_Principales_1__c'],axis = 1)

df.to_excel("Archivo_filtrado.xlsx") #Almacena la informacion en un archivo excel.

if df.empty:
    print('No se encontraron datos con el filtro indicado. ')
else:
    print('Los datos han sido exportados al Archivo_filtrado en formato xlsx')