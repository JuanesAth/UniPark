import requests
import pandas as pd

# Especificar la latitud y longitud de la ubicación de Rionegro, Antioquia, CO
latitud = 6.1554
longitud = -75.3736

# Reemplaza 'tu_api_key' con tu clave de API de OpenWeatherMap
api_key = '352567e1b89c7c9019105f43b3e36239'

# URL de la API de OpenWeatherMap para obtener la previsión horaria de 4 días
url = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitud}&lon={longitud}&cnt=96&appid={api_key}'
#https://api.openweathermap.org/data/2.5/forecast/hourly?lat=6.1554&lon=-75.3736&appid=352567e1b89c7c9019105f43b3e36239

# Realizar la solicitud GET a la API para obtener la previsión horaria
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    forecasts = data['list']

    # Crear una lista para almacenar los datos del clima por hora
    clima_por_hora = []

    # Recorrer los datos y guardarlos en la lista
    for forecast in forecasts:
        timestamp = forecast['dt_txt']
        estado_clima = forecast['weather'][0]['main']
        clima_por_hora.append({
            'fecha': timestamp,
            'estado_clima': estado_clima
        })

    # Convertir la lista en un DataFrame
    df = pd.DataFrame(clima_por_hora)

    # Ahora tienes un DataFrame con los datos del clima por hora
    print(df)
else:
    print('No se pudo obtener la información de la previsión horaria.')


