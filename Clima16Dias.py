import requests
import pandas as pd

# Especificar la latitud y longitud de la ubicación de Rionegro, Antioquia, CO
lat = 6.1554
lon = -75.3736

# Cantidad de días para la previsión (ajusta según tus necesidades)
cnt = 7

# Reemplaza 'tu_api_key' con tu clave de API de OpenWeatherMap
API_key = '352567e1b89c7c9019105f43b3e36239'

# URL de la API de OpenWeatherMap para obtener la previsión diaria
url = f'https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={cnt}&appid={API_key}'

#https://api.openweathermap.org/data/2.5/forecast/daily?lat=6.1554&lon=-75.3736&cnt=7&appid=352567e1b89c7c9019105f43b3e36239

# Realizar la solicitud GET a la API para obtener la previsión diaria
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    forecasts = data['list']

    # Crear una lista para almacenar los datos del día y el clima
    clima_por_dia = []

    # Recorrer los datos y guardar el día y el clima
    for forecast in forecasts:
        timestamp = forecast['dt']
        day = pd.to_datetime(timestamp, unit='s').date()
        weather_description = forecast['weather'][0]['description']
        clima_por_dia.append({
            'dia': day,
            'descripcion_clima': weather_description
        })

    # Convertir la lista en un DataFrame
    df = pd.DataFrame(clima_por_dia)

    # Ahora tienes un DataFrame con los datos del día y el clima
    print(df)
else:
    print('No se pudo obtener la información de la previsión diaria.')
