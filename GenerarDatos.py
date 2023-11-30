import pandas as pd
import numpy as np

datos_por_semana = []

for semana in range(32):  # 32 semanas de datos
    semana_data = []

    for dia in [1, 2, 3, 4, 5]:  # Días Lunes(1), Martes(2), Miercoles(3), Jueves4 y Vienes(5) en ese orden
        for hora in range(12, 21):  # Horas de 12 a 20 en ese orden
            """
            Climas que no afectan las plazas de parqueo (0)
            Despejado 0.15
            Nublado 0.25
            Parcialmente Nublado 0.25
            __________________________
            Total = 0.65
    
            Climas que aumentan en gran medida el parqueo (1)
            Lluvia 0.15
            TormentaElectrica 0.08
            Llovizna 0.12
            _________________________
            Total = 0.25
            """
            clima = np.random.choice([0, 1], p=[0.65, 0.35])  
            if hora < 15:
                plazas_ocupadas = np.where(clima == 0, np.random.randint(10, 20), np.random.randint(20, 33))
            elif 15 <= hora < 18:
                plazas_ocupadas = np.where(clima == 0, np.random.randint(27, 37), np.random.randint(35, 45))
            else:
                plazas_ocupadas = np.where(clima == 0, np.random.randint(45, 50), np.random.randint(48, 50))
            # Calcula las plazas libres restando de 50 las plazas ocupadas
            plazas_libres = 50 - plazas_ocupadas
            registro = {
                'Dia': dia,
                'Hora': hora,
                'Clima': clima,
                'Plazas Ocupadas': plazas_ocupadas,
                'Plazas Libres': plazas_libres  # Agrega la columna "Plazas Libres"
            }
            semana_data.append(registro)

    datos_por_semana.extend(semana_data)

# Convertir los datos en un DataFrame de pandas
data_frame = pd.DataFrame(datos_por_semana)

# Guardar el DataFrame en un archivo CSV
data_frame.to_csv('datos_registros.csv', index=False)
