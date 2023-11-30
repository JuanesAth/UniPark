import os
import requests

from dotenv import load_dotenv

load_dotenv()

# Definir tu clave de API de OpenWeatherMap
api_key = os.getenv('api_key')
# Especificar la latitud y longitud de la ubicación de Rionegro, Antioquia, CO
latitud = 6.1554
longitud = -75.3736

"""
# Especificar la ciudad de Rionegro, Colombia
ciudad = 'Rionegro'
estado = 'Antioquia'
pais = 'CO'

#Codigo para averiguar la latitud y longitud de la ciudad

# Especificar el límite (1 en este caso)
limit = 1

# URL de la API de OpenWeatherMap para buscar la ubicación geográfica
url = f'http://api.openweathermap.org/geo/1.0/direct?q={ciudad},{pais}&limit={limit}&appid={api_key}'

# Realizar la solicitud GET a la API para buscar la ubicación geográfica
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()

    # Verificar si se encontró una ubicación
    if data:
        # Obtener la información de la ubicación encontrada
        ubicacion = data[0]
        latitud = ubicacion['lat']
        longitud = ubicacion['lon']

        # Imprimir la ubicación encontrada
        print(f'Ubicación encontrada para {ciudad}, {estado}, {pais}:')
        print(f'Latitud: {latitud}')
        print(f'Longitud: {longitud}')

        # Usar la información de ubicación para obtener el estado del clima (puedes usar la latitud y longitud)
        # Agregar aquí la lógica para obtener el estado del clima utilizando la latitud y longitud
    else:
        print(f'No se encontró una ubicación para {ciudad}, {estado}, {pais}.')
else:
    print('No se pudo realizar la búsqueda de ubicación.')"""

def obtener_clima_binario(latitud, longitud, api_key):
    # URL de la API de OpenWeatherMap para obtener el clima actual en función de la latitud y longitud
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={api_key}'

    # Realizar la solicitud GET a la API para obtener el estado del clima actual
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        # Extraer el estado del clima actual
        estado_clima = data['weather'][0]['main']

        print(f"Clima Actual: {estado_clima}")
        # Definir una lista de estados de mal clima
        mal_clima = ['Rain', 'Thunderstorm', 'Snow', 'Sleet', 'Hail', 'Fog']

        # Clasificar el clima como 0 o 1
        clima_binario = 1 if estado_clima in mal_clima else 0

        # Retornar el resultado
        return clima_binario
    else:
        print('No se pudo obtener la información del clima actual.')
        return None



