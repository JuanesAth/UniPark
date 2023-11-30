from tkinter import messagebox, ttk
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import tkinter as tk
from tkinter import Label, Entry
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3

from ClimaActual import obtener_clima_binario
from Dia_y_Hora import obtener_dia_y_hora

"""
# Cargar los datos desde un archivo CSV
data = pd.read_csv("datos_registros.csv")

# Crear la conexión a la base de datos SQLite
conn = sqlite3.connect('datos_registros.db')

# Guardar el DataFrame en la tabla 'datos_registros'
data.to_sql('datos_registros', conn, index=False, if_exists='replace')

# Cerrar la conexión a la base de datos
conn.close()
"""

# Abrir conexión para realizar la consulta
conn = sqlite3.connect('bd/datos_registros.db')

# Consulta SQL para obtener las características (X) y etiquetas (y)
query = "SELECT Dia, Hora, Clima, [Plazas Ocupadas] FROM datos_registros"

# Obtener los datos desde la base de datos
data_from_db = pd.read_sql_query(query, conn)

# Cerrar la conexión a la base de datos
conn.close()

# División de datos en características (X) y etiquetas (y) desde la base de datos
X = data_from_db[['Dia', 'Hora', 'Clima']]
y = data_from_db['Plazas Ocupadas']

# Búsqueda y evaluación de diferentes modelos

# Regresión de Bosque Aleatorio
modelo_RF = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_RF.fit(X, y)
predicciones_RF = modelo_RF.predict(X)

# Regresión Ridge
modelo_Ridge = Ridge(alpha=1.0)
modelo_Ridge.fit(X, y)
predicciones_Ridge = modelo_Ridge.predict(X)

# Regresión Lasso
modelo_Lasso = Lasso(alpha=1.0)
modelo_Lasso.fit(X, y)
predicciones_Lasso = modelo_Lasso.predict(X)

# Regresión Polinómica
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
modelo_Polinomica = LinearRegression()
modelo_Polinomica.fit(X_poly, y)
predicciones_Polinomica = modelo_Polinomica.predict(X_poly)

# Regresión Lineal
modelo_Lineal = LinearRegression()
modelo_Lineal.fit(X, y)
predicciones_Lineal = modelo_Lineal.predict(X)

# Red Neuronal
modelo_RN = MLPRegressor(hidden_layer_sizes=(100, 100), max_iter=1000)
modelo_RN.fit(X, y)
predicciones_RN = modelo_RN.predict(X)

# Regresión de Vecinos Más Cercanos
modelo_KNN = KNeighborsRegressor(n_neighbors=3) 
modelo_KNN.fit(X, y)
predicciones_KNN = modelo_KNN.predict(X)

# Diccionario de los Resultados de la evaluación
resultados = {
    "Regresión de Bosque Aleatorio": {"MSE": mean_squared_error(y, predicciones_RF),"R^2": r2_score(y, predicciones_RF)},
    "Regresión Ridge": {"MSE": mean_squared_error(y, predicciones_Ridge),"R^2": r2_score(y, predicciones_Ridge)},
    "Regresión Lasso": {"MSE": mean_squared_error(y, predicciones_Lasso),"R^2": r2_score(y, predicciones_Lasso)},
    "Regresión Polinómica": {"MSE": mean_squared_error(y, predicciones_Polinomica),"R^2": r2_score(y, predicciones_Polinomica)},
    "Regresión Lineal": {"MSE": mean_squared_error(y, predicciones_Lineal),"R^2": r2_score(y, predicciones_Lineal)},
    "Red Neuronal": {"MSE": mean_squared_error(y, predicciones_RN),"R^2": r2_score(y, predicciones_RN)},
    "Regresión de Vecinos Más Cercanos": {"MSE": mean_squared_error(y, predicciones_KNN),"R^2": r2_score(y, predicciones_KNN)}
}

# Imprimir resultados
for modelo, resultado in resultados.items():
    print(f"{modelo}:")
    print(f"  - Error Cuadrático Medio (MSE): {resultado['MSE']:.2f}")
    print(f"  - Coeficiente de Determinación (R^2): {resultado['R^2']:.2f}")
    print()

# Creación de la aplicación tkinter
app = tk.Tk()
app.title("UniPark")
app.iconbitmap("image/aparcamiento.ico")

# Creación de marcos para organizar elementos de la interfaz
marco_izquierdo = tk.Frame(app)
marco_izquierdo.grid(row=0, column=0, padx=100, pady=100)

marco_derecho = tk.Frame(app)
marco_derecho.grid(row=0, column=1, padx=10, pady=10)

#Label para mostrar la probabilidad de encontrar parqueadero
porcentaje_prob = tk.StringVar()
labelPorcentaje = tk.Label(marco_izquierdo, textvariable=porcentaje_prob, font=("Helvetica", 16))
labelPorcentaje.pack()

# Separador
sep = ttk.Separator(marco_izquierdo, orient='horizontal')
sep.pack(fill='x', pady=10)

# Creación de etiquetas y campos de entrada para día, hora y clima
Label(marco_izquierdo, text="Día:", font=("Helvetica", 14)).pack()
dia_entry = Entry(marco_izquierdo,font=("Helvetica", 14))
dia_entry.pack()
Label(marco_izquierdo, text="Hora:", font=("Helvetica", 14)).pack()
hora_entry = Entry(marco_izquierdo, font=("Helvetica", 14))
hora_entry.pack()
Label(marco_izquierdo, text="Clima:", font=("Helvetica", 14)).pack()
clima_entry = Entry(marco_izquierdo,font=("Helvetica", 14))
clima_entry.pack()

# Creación de un widget de gráfico en el marco derecho
fig = Figure(figsize=(8, 6))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=marco_derecho)
canvas.get_tk_widget().pack()

# Función para realizar la predicción y actualizar el gráfico
def predecir_y_graficar():
    dia = dia_entry.get()
    hora = hora_entry.get()
    clima = clima_entry.get()
    
    # Verificar si los campos están vacíos
    if dia == '' or hora == '' or clima== '':
        # Uno o más campos están vacíos
        mensaje = "Uno o más campos están vacíos"
        messagebox.showinfo("Campos vacíos", mensaje)
    else:
        if (dia.isdigit()) and (hora.isdigit()) and (clima.isdigit()):
                
            dia = int(dia)
            hora = int(hora)
            clima = int(clima)
            
            if 12<=hora<=20 and 1<=dia<=5 and 0<=clima<=1:
                # Creación de un DataFrame para realizar la predicción
                variables_a_predecir = pd.DataFrame({'Dia': [dia], 'Hora': [hora], 'Clima': [clima]})
                prediccion = modelo_KNN.predict(variables_a_predecir)

                # Filtrado de datos que coinciden con las variables de entrada (Día, Hora, Clima)
                datos_filtrados = data_from_db[(data_from_db['Dia'] == dia) & (data_from_db['Hora'] == hora) & (data_from_db['Clima'] == clima)]

                # Actualización del gráfico
                ax.clear()
                ax.plot(datos_filtrados.index, datos_filtrados['Plazas Ocupadas'], label='Datos Filtrados', color='green', marker='o')
                ax.scatter(1460, prediccion, label=f'Predicción: {prediccion[0]:.1f}', color='red', s=100)

                probabilidad_final = 100-((100*prediccion[0])/50)
                porcentaje_prob.set(f"La probabilidad de encontrar parqueadero es del\n{probabilidad_final:.1f}%")
                consejos_finales = func_consejos(probabilidad_final, clima)
                label_consejos.set(consejos_finales)
        
                ultimo_punto_morado = datos_filtrados.iloc[-1]
                ax.plot([datos_filtrados.index[-1], 1460], [ultimo_punto_morado['Plazas Ocupadas'], prediccion[0]], '--', linewidth=1, color='red')
                ax.text(1460, prediccion[0], f'{prediccion[0]:.1f}', fontsize=12, color='red', verticalalignment='bottom')

                ax.set_xlabel('Índice de Datos Filtrados')
                ax.set_ylabel('Plazas Ocupadas')
                ax.set_title(f'Comparación de Datos Filtrados y Predicción (Dia {dia}, Hora {hora} con {"Mal clima" if clima == 1 else "Buen clima" })')
                ax.legend()
                ax.grid(True)
                ax.set_ylim(0, 50)

                canvas.draw()
            else:
                mensaje = "Algunos datos digitados estan mal. \n Dia entre 1-5 (LUNES a VIERNES)\n Hora entre 12-20 (12 a 8 pm) \n Clima (0 -> Buen clima o 1-> Mal clima)"
                messagebox.showinfo("Datos Erroneos", mensaje)
                
        else:
            mensaje = "Algunos datos digitados no son Numericos. \n Dia entre 1-5 (LUNES a VIERNES)\n Hora entre 12-20 (12 a 8 pm) \n Clima (0 -> Buen clima o 1-> Mal clima)"
            messagebox.showinfo("Datos Erroneos", mensaje)

# Función para realizar la predicción y actualizar el gráfico
def predecir_y_graficar_DiaActual():
    dia, hora = obtener_dia_y_hora()
    if 12<=hora<=20 and 1<=dia<=5:
        api_key = '352567e1b89c7c9019105f43b3e36239'
        latitud = 6.1554
        longitud = -75.3736
        clima = obtener_clima_binario(latitud, longitud, api_key)

        # Creación de un DataFrame para realizar la predicción
        variables_a_predecir = pd.DataFrame({'Dia': [dia], 'Hora': [hora], 'Clima': [clima]})
        prediccion = modelo_KNN.predict(variables_a_predecir)

        # Filtrado de datos que coinciden con las variables de entrada (Día, Hora, Clima)
        datos_filtrados = data_from_db[(data_from_db['Dia'] == dia) & (data_from_db['Hora'] == hora) & (data_from_db['Clima'] == clima)]

        # Actualización del gráfico
        ax.clear()
        ax.plot(datos_filtrados.index, datos_filtrados['Plazas Ocupadas'], label='Datos Filtrados', color='green', marker='o')
        ax.scatter(1460, prediccion, label=f'Predicción: {prediccion[0]:.1f}', color='red', s=100)

        probabilidad_final = 100-((100*prediccion[0])/50)
        porcentaje_prob.set(f"La probabilidad de encontrar parqueadero es del\n{probabilidad_final:.1f}%")
        consejos_finales = func_consejos(probabilidad_final, clima)
        label_consejos.set(consejos_finales)
        
        ultimo_punto_morado = datos_filtrados.iloc[-1]
        ax.plot([datos_filtrados.index[-1], 1460], [ultimo_punto_morado['Plazas Ocupadas'], prediccion[0]], '--', linewidth=1, color='red')
        ax.text(1460, prediccion[0], f'{prediccion[0]:.1f}', fontsize=12, color='red', verticalalignment='bottom')

        ax.set_xlabel('Índice de Datos Filtrados')
        ax.set_ylabel('Plazas Ocupadas')
        ax.set_title(f'Comparación de Datos Filtrados y Predicción (Dia {dia}, Hora {hora} con {"Mal clima" if clima == 1 else "Buen clima" })')
        ax.legend()
        ax.grid(True)
        ax.set_ylim(0, 50)

        canvas.draw()
    else:
        mensaje = "Esta función solo se puede utilizar de Lunes a Viernes entre las 12 y las 8 pm"
        messagebox.showinfo("Fuera de servicio", mensaje) 
        
# Botón para realizar la predicción y actualizar el gráfico
button1 = tk.Button(marco_izquierdo, text="Realizar Predicción", command=predecir_y_graficar,
                    bg="green", fg="white", padx=10, pady=5, font=("Helvetica", 12))
button1.pack(pady=10)

# Botón 2: Predicción Actual
button2 = tk.Button(marco_izquierdo, text="Predicción Actual", command=predecir_y_graficar_DiaActual,
                    bg="green", fg="white", padx=10, pady=5, font=("Helvetica", 12))
button2.pack(pady=10)

#Label para mostrar la probabilidad de encontrar parqueadero
label_consejos = tk.StringVar()
lbl_consejos = tk.Label(marco_izquierdo, textvariable=label_consejos, font=("Helvetica", 10))
lbl_consejos.pack()

def func_consejos(prob_encontrar, clima):
    consejos = ""

    if prob_encontrar > 80:
        consejos += "La probabilidad de encontrar parqueadero es muy alta. \n¡Genial! Puedes considerar utilizar tu vehículo sin preocupaciones.\n\n"
    if 70 < prob_encontrar <= 90 and clima == 1:
        consejos += "Dado que la probabilidad de encontrar parqueadero es \nalta y el clima no acompaña, te recomendamos buscar un parqueadero externo con anticipación.\n\n"
    if 35 < prob_encontrar <= 70 and clima == 0:
        consejos += "Aunque la probabilidad de encontrar parqueadero es moderada, \nes posible que encuentres espacio para tu vehículo. No te preocupes demasiado.\n\n"
    if 30 <= prob_encontrar < 55 and clima == 0:
        consejos += "La probabilidad de encontrar parqueadero es moderada. \nConsidera explorar opciones de transporte compartido para evitar complicaciones.\n\n"
    if prob_encontrar < 40 and clima == 1:
        consejos += "Aunque la probabilidad de encontrar parqueadero es baja, \nten en cuenta que el clima no es favorable. \nPlanifica con anticipación para buscar un parqueadero externo.\n\n"
    if prob_encontrar > 70 and clima == 0:
        consejos += "Dado que la probabilidad de encontrar parqueadero es alta y \nel clima es bueno, podrías considerar opciones alternativas como la \nbicicleta o transporte compartido.\n\n"
    if 35 < prob_encontrar <= 60 and clima == 1:
        consejos += "La probabilidad de encontrar parqueadero es moderada y el \nclima es desfavorable. Planifica con anticipación y considera opciones \nde transporte público.\n\n"
    if prob_encontrar<=10:
        consejos += "La probabilidad de encontrar parqueadero es muy baja.\n Te recomendamos explorar opciones de transporte público o buscar alternativas\n como estacionamientos cercanos.\n\n"

    return consejos

# Iniciar la aplicación tkinter
app.mainloop()
