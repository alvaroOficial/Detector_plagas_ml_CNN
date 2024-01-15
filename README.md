# Detector_plagas_ml_CNN
## Clasificar e identificar las plagas en cultivos a partir de fotos.
![](https://github.com/alvaroOficial/Detector_plagas_ml_CNN/blob/main/esquema.png)
## EJECUCIÓN
Se tienen dos partes para el código; en la primera parte se entrena el modelo con las imágenes del dataset.<br>
 a) Haber instalado las librerías necesarias para redes CNN como tensorflow,keras.<br>
 b) Descargar y ubicar correctamente el dataset.<br>
 c) abrir el archivo modelo_entrennamiento.ipynb; reemplazar las rutas y ejecutarlo.<br>
 d) Entrenar el modelo con el dataset y parametros a decisión.<br>
 d) se tendrá como salida dos archivos .h5 con el modelo y sus pesos.<br>

 --------------------------------------------------------------------------------
Para la segunda parte se ejecuta el modelo ya entrenado y se crea el local host con streamlit:<br>
 se recomienda tener las librerías de streamlit.<br>
 e) Abrir el archivo salida.py<br>
 d) Ubicar correctamente la ruta de modelo.h5 y de pesos.h5<br>
 e) una vez se ejecute correctamente, se debe abrir el local host desde la terminal.<br>
 d)Finalmente seleccione la cantidad y suba las imágenes a detectar, si desea puede descargar un archivo csv con los diagnósticos.<br>
 
## Conclusiones
Es importante tener en cuenta que resulta útil entrenar primero el archivo y posteriormente tomar ese modelo ya entrenado, pues reduce demasiado el tiempo de procesamiento y permite crear un código mucho más amigable y sencillo por ejemplo en este caso en la interfaz gráfica.<br>
En síntesis, si bien se obtuvo un accuracy entre el 0.88 y el 0.9 en el modelo variando parámetros, se puede decir que la clasificación dentro de las tres clases es bastante buena, sin embargo algo a considerar es que en la sección de insectos, tiende a ocurrir más errores debido a la gran variedad de especies, débil cantidad de datos de entrenamiento.<br>
Por otra parte, resulta útil un proyecto de Convolutional Neural Network (CNN) diseñado para clasificar enfermedades en cultivos ofrece beneficios significativos en la agricultura. Permitiendo la detección temprana de enfermedades, optimizando el uso de pesticidas, aumentando la productividad agrícola y reduciendo costos, contribuye a prácticas agrícolas más sostenibles. Este enfoque eficiente también facilita decisiones informadas para los agricultores, especialmente en áreas con recursos limitados, y sirve como una valiosa herramienta educativa. En resumen, el proyecto mejora la salud de los cultivos, la eficiencia en la gestión agrícola y tiene un impacto positivo en la sostenibilidad y productividad agrícolas.
 
