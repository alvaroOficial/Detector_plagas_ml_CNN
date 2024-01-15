from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import streamlit as st
from PIL import Image
import cv2
import pandas as pd
import base64
import random

longitud, altura = 150, 100
#importar el modelo y los pesos
modelo_path = 'C:\\Users\\jamer\\Downloads\\modelo.h5'
pesos_modelo_path = 'C:\\Users\\jamer\\Downloads\\pesos.h5'
cnn = load_model(modelo_path)
cnn.load_weights(pesos_modelo_path)

# Configurar interfaz
st.markdown("# Bienvenido a 0P: ")
st.markdown("## 0 plagas; 0 perdidas")
st.markdown("Detecta las plagas de tus cultivos tan solo con imágenes y exporta los datos del diagnóstico si así lo deseas.")

# Solicitar al usuario la cantidad de fotos a subir
cantidad_fotos = st.number_input("Seleccione la cantidad de fotos a subir", min_value=1, value=1, step=1)

# List para almacenar las imágenes cargadas
uploaded_files = st.file_uploader("Carga aquí las fotos de tus cultivos", type=["jpg", "jpeg", "png"], key="uploader", accept_multiple_files=True)

# Texto para el diagnóstico
diagnostico_texto = st.empty()

# DataFrame para almacenar los resultados
resultados_df = pd.DataFrame(columns=["Imagen", "Diagnostico"])

# Lista para almacenar índices de imágenes para mostrar al azar
indices_a_mostrar = random.sample(range(cantidad_fotos), min(cantidad_fotos, 2))

# Función para realizar la predicción en una imagen
def predict(image, image_name):
    # Convertir la imagen a un formato que pueda ser procesado por el modelo
    image = image.resize((altura, longitud))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)

    # Realizar la predicción
    predictions = cnn.predict(image_array)
    result = predictions[0]
    answer = np.argmax(result)

    # Mapear el diagnóstico a palabras
    diagnosis_mapping = {0: "Cultivo Enfermo", 1: "Peste-insectos", 2: "Cultivo Sano"}
    diagnosis_word = diagnosis_mapping.get(answer, "Desconocido")

    # Actualizar el DataFrame con los resultados
    resultados_df.loc[len(resultados_df)] = [image_name, diagnosis_word]

    # Mostrar la imagen procesada junto con el diagnóstico
    if len(resultados_df) - 1 in indices_a_mostrar:
        st.image(image, caption=f"Diagnóstico: {diagnosis_word}", use_column_width=True, width=100)  # Ajusta el valor de 'width'

# Botón para realizar la predicción con las imágenes cargadas
if st.button("Realizar Predicción") and uploaded_files:
    for i in range(cantidad_fotos):
        if i < len(uploaded_files):
            image = Image.open(uploaded_files[i])
            predict(image, uploaded_files[i].name)

    # Mostrar el diagnóstico en un DataFrame
    st.dataframe(resultados_df)

    # Botón para descargar el archivo CSV
    csv_file = resultados_df.to_csv(index=False)
    b64 = base64.b64encode(csv_file.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="resultados.csv">Descargar Resultados como CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

# Botón para tomar una foto desde la cámara
if st.button("Diagnostico Rapido"):
    # Abrir la conexión a la cámara
    cap = cv2.VideoCapture(0)

    # Tomar una foto
    ret, frame = cap.read()
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    # Mostrar la foto y realizar la predicción
    st.image(image, channels="RGB", use_column_width=True)
    predict(image, "foto_desde_camara")

    # Cerrar la conexión a la cámara
    cap.release()

    ##by Alvaro Hernandez













