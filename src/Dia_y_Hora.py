from datetime import datetime

def obtener_dia_y_hora():
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()

    # Obtener el número del día de la semana (lunes = 1, martes = 2, ..., domingo = 7)
    numero_dia_semana = fecha_hora_actual.weekday() + 1

    # Obtener solo la hora
    hora_actual = int(fecha_hora_actual.strftime("%H"))

    # Retornar los valores
    return numero_dia_semana, hora_actual

# Llamar a la función y obtener los valores
dia, hora = obtener_dia_y_hora()

# Imprimir los valores
"""
print("Día de la semana:", dia)
print("Hora actual:", hora)
"""


