# UniPark

UniPark es un proyecto que utiliza el modelo de Regresión KNN para calcular la probabilidad de encontrar un parqueadero, teniendo en cuenta diversos datos como el día, la hora, el clima y las plazas ocupadas.

## API Reference

### ClimaActual.py

Esta sección describe el archivo `ClimaActual.py`, el cual proporciona información climática actual mediante la API de OpenWeatherMap.

#### Parámetros:

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Requerido**. Tu clave de API para OpenWeatherMap |
| `latitud` | `int`    | **Requerido**. Tu latitud |
| `longitud` | `int`   | **Requerido**. Tu longitud |

```http
http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={api_key}
```

**Openweathermap:** https://openweathermap.org/api# UniPark

