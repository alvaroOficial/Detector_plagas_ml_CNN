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
Es importante tener en cuenta que resulta util entrenar primero el archivo y luego tomar ese modelo, pues reduce demasiado el tiemo de procesamiento y permite crear un codigo mucho mas amigable y sencillo por ejemplo en este caso en la interfaz grafica.
En sintesis si bien se obtuvo un accuracy entre el 0.88 y el 0.9 en el modelo variando parametros, se puede decir que la clasificación dentro de las tres clases es bastante buena, sin embargo algo a considerar es que en la seccion de insectos, tiende a ocurrir mas errores debido a la gran variedad, cantidad de datos de entrenamiento.
Por otra parte resulta util Un proyecto de Convolutional Neural Network (CNN) para clasificar enfermedades en cultivos tiene utilidades clave, como la detección temprana de enfermedades, la optimización del uso de pesticidas, el aumento de la productividad agrícola, la reducción de costos y la promoción de prácticas agrícolas sostenibles. Además, facilita la toma de decisiones informadas para los agricultores, especialmente en regiones con recursos limitados, y sirve como una herramienta educativa para abordar eficazmente los problemas de enfermedades en los cultivos.


 
