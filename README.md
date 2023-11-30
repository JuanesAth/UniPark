# UniPark
Proyecto el cual arroja la probabilidad de Encontrar parqueadero según los datos suministrados (Dia, Hora, Clima, Plazas ocupadas), con el Modelo de Regresión KNN.



## API Reference
```http
```
**ClimaActual.py**
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Tu API key |
| `latitud` | `int` | **Required**. Tu Latitud |
| `longitu` | `int` | **Required**. Tu Longitud |

API call: http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={api_key}



**Openweathermap:** https://openweathermap.org/api
