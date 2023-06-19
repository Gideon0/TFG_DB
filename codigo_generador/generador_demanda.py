import random
import json
import os

# Lista de barrios en Valencia (18)
ubicaciones = ["Ciutat Vella", "Eixample", "Extamurs", "Campanar", "La Saidia", "El Pla del Real", "L'Olivereta", "Patraix", "Jesus", "Quatre Carreres", 
               "Poblats Maritims", "Camins al Grau", "Algiros", "Benimaclet", "Rascanya", "Benicalap", "Pobles del Nord", "Pobles de l'Oest"]

#Lista de tipos de la demanda (21)
tipos_demanda = ["Cirujano", "Traumatologo", "Ginecologo", "Bombero Forestal", "Bombero Ayuntamiento", "Bombero Militar", "Inspector", "Comisario", "Jefe Superior", 
         "Camion Bomba", "Camion Sisterna", "Ambulancia Individual", "Ambulancia Colectiva", "Vehiculo de Asistencia Medica", "Unidad de Rescate", "Patrulla",
         "Medico", "Bombero", "Policia", "Vehiculo grande", "Vehiculo pequenyo"]

total_combinaciones = len(ubicaciones) * len(tipos_demanda)

for nivel in range(1, 4):
  if nivel == 1:
    numero = 20
  elif nivel == 2:
    numero = 40
  elif nivel == 3:
    numero = 60 
  for i in range(1, 6):
    demanda = []
    combinaciones = set()
    while len(demanda) < numero:
        ubicacion = random.choice(ubicaciones)
        tipo = random.choice(tipos_demanda)
        combinacion = (ubicacion, tipo)
        if combinacion not in combinaciones:
          cantidad = random.randint(1,5)
          horas = random.randint(1, 8)
          prioridad = random.randint(1,5)
          demanda.append({
              'Ubicacion': ubicacion,
              'Tipo': tipo,
              'Cantidad': cantidad,
              'Horas': horas,
              'Prioridad': prioridad
          })
          combinaciones.add(combinacion)

    # Guardar los datos en un archivo de texto
    nombre = 'demanda' + str(i) + '.json'
    carpeta = 'nivel ' + str(nivel)
    if not os.path.exists(carpeta):
       os.makedirs(carpeta)
    ruta_archivo = os.path.join(carpeta, nombre)
    with open(ruta_archivo, 'w') as archivo:
        json.dump(demanda, archivo)

  print("Se han generado 5 bases de datos de demanda, nivel " + str(nivel))