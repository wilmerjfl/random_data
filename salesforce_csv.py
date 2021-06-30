import csv
import random as r
import names
import randominfo

domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online", "omega", "institute", "finance", "company", "corporation", "community"]
extentions = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'co', 'me', 'biz', 'dev', 'ngo', 'site', 'xyz', 'zero', 'tech']
	
def crearCsv(info):
  with open('salida.csv', 'w', newline='') as filename:
    file = csv.writer(filename, delimiter=',')
    for i in info:
      file.writerow(i)

def generateCsvInfo():
  info = []
  sex = {
    'male': 'Hombre',
    'female': 'Mujer'
  }
  antecedentes = ['si','no']
  categoria =['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4', 'Categoria 5', 'Categoria 6','Categoria 7']
  consume = ['si','no']
  detalle = ['Detalle de zona A', 'Detalle de zona b', 'Detalle de zona c', 'Detalle de zona d', 'Detalle de zona e','Detalle de zona f']
  estado = ['ACTIVO','BAJA','INCORPORADO PERMANENTE','NO ADMITIDO']
  oficios = ['Oficios Principales 2','Oficios Principales 3', 'Oficios Principales 4', 'Oficios Principales 5','Oficios Principales 6','Oficios Principales 7','Oficios Principales 8']
  oficios2 = ['Oficios 1', 'Oficios 2', 'Oficios 3', 'Oficios 4', 'Oficios 5', 'Oficios 6','Oficios 7']
  oficios3 = ['Oficio A','Oficio N','Oficio Z','Oficio S','Oficio D','Oficio F','Oficio G']
  zona = ['zona_a','zona_b','zona_c','zona_d','zona_e','zona_f','zona_g']
  zona_trabajo = ['Zona de trabajo Preferibles A','Zona de trabajo Preferibles B','Zona de trabajo Preferibles C','Zona de trabajo Preferibles F','Zona de trabajo Preferibles G','Zona de trabajo Preferibles J']
 
  for i in range(1000):
    nombre = randominfo.get_first_name()
    apellido = names.get_last_name()
    email = nombre + apellido + '@' + r.choice(domains) + '.' + r.choice(extentions)
    #fecha_nac = randominfo.get_birthdate(startAge = 18, endAge=50, _format = '%d %b %Y')
    numero_usuario = r.randint(10000000,90000000)
    try:
      sexo = sex[randominfo.get_gender(nombre)]
    except:
      sexo = 'Hombre'
    telefono = randominfo.get_phone_number(91)
    info.append([nombre,apellido,r.choice(antecedentes),r.choice(categoria),r.choice(consume),r.choice(detalle),email,r.choice(estado),numero_usuario,r.choice(oficios),r.choice(oficios2),r.choice(oficios3),sexo,telefono,r.choice(zona),r.choice(zona_trabajo)])
    crearCsv(info)

generateCsvInfo()