import random
import json
import os
import string
from faker import Faker

faker = Faker()
# Lista de barrios en Valencia (19)
ubicaciones = ["Ciutat Vella", "Eixample", "Extamurs", "Campanar", "La Saidia", "El Pla del Real", "L'Olivereta", "Patraix", "Jesus", "Quatre Carreres", 
               "Poblats Maritims", "Camins al Grau", "Algiros", "Benimaclet", "Rascanya", "Benicalap", "Pobles del Nord", "Pobles de l'Oest", "Pobles del Sud"]

# Lista de tipos posibles de la oferta (16)
tipos = ["Cirujano", "Traumatologo", "Ginecologo", "Bombero Forestal", "Bombero Ayuntamiento", "Bombero Militar", "Inspector", "Comisario", "Jefe Superior", 
         "Camion Bomba", "Camion Sisterna", "Ambulancia Individual", "Ambulancia Colectiva", "Vehiculo de Asistencia Medica", "Unidad de Rescate", "Patrulla"]

# Lista de tipos genericos posibles de la oferta (5)
tipos_genericos = ["Medico", "Bombero", "Policia", "Vehiculo grande", "Vehiculo pequenyo"]

# Función para generar un identificador aleatorio
def generar_identificador(tipo_generico):
  if(tipo_generico == 'Medico' or tipo_generico == 'Bombero' or tipo_generico == 'Policia'):
    return faker.first_name()
    
  else: 
    numero_matricula = faker.random_int(min=1000, max=9999)
    letras_matricula = ''.join(random.choices(string.ascii_uppercase, k=3))
    matricula = f"{letras_matricula}-{numero_matricula}"
    return matricula


# Generar datos
nivel = 4
numero = 35000 
for i in range(1, 6):
  oferta = []
  combinaciones = set()
  matriculas = set()
  contador = 0
  while len(oferta) < numero:
    tipo = random.choice(tipos)
    tipo_index = tipos.index(tipo)
    if(tipo_index >= 0 and tipo_index <= 2):
      Tipo_Generico = "Medico"
    elif(tipo_index >= 3 and tipo_index <= 5):
      Tipo_Generico = "Bombero"
    elif(tipo_index >= 6 and tipo_index <= 8):
      Tipo_Generico = "Policia"
    elif(tipo_index >= 9 and tipo_index <= 12):
      Tipo_Generico = "Vehiculo grande"
    elif(tipo_index >= 13 and tipo_index <= 15):
      Tipo_Generico = "Vehiculo pequenyo"
      
    identificador = generar_identificador(Tipo_Generico)
    ubicacion = random.choice(ubicaciones)
    combinacion = (ubicacion, identificador, tipo) 
    matricula = (identificador)
    if ((Tipo_Generico == "Medico" or Tipo_Generico == "Policia" or Tipo_Generico == "Bombero") and combinacion not in combinaciones):
      horas = random.randint(1, 8)
      coste = random.randint(6, 10)
      oferta.append({
          'Ubicacion': ubicacion,
          'Identificador': identificador,
          'Tipo': tipo,
          'Tipo Generico': Tipo_Generico,
          'Horas': horas,
          'Coste': coste
      })
      combinaciones.add(combinacion)
      contador = contador + 1

    elif((Tipo_Generico == "Vehiculo grande" or Tipo_Generico == "Vehiculo pequenyo") and matricula not in matriculas):
      horas = random.randint(1, 8)
      coste = random.randint(6, 10)
      oferta.append({
          'Ubicacion': ubicacion,
          'Identificador': identificador,
          'Tipo': tipo,
          'Tipo Generico': Tipo_Generico,
          'Horas': horas,
          'Coste': coste
      })
      matriculas.add(matricula)
      contador = contador + 1
  # Guardar los datos en un archivo de texto
  nombre = 'oferta' + str(i) + '.json'
  carpeta = 'nivel ' + str(nivel)
  if not os.path.exists(carpeta):
      os.makedirs(carpeta)
  ruta_archivo = os.path.join(carpeta, nombre)
  with open(ruta_archivo, 'w') as archivo:
      json.dump(oferta, archivo)

print("Se han generado 5 bases de datos de oferta, nivel " + str(nivel))