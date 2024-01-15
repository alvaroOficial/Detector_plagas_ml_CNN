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
Para la segunda parte e ejecuta el modelo ya entrenado y se crea el local host:<br>
 se recomienda tener las librerías de streamlit.<br>
 e) Abrir el archivo salida.py<br>
 d) Ubicar correctamente la ruta de modelo.h5 y de pesos.h5<br>
 e) una vez se ejecute correctamente, se debe abrir el local host desde la terminal.<br>
 d)Finalmente seleccione la cantidad y suba las imágenes a detectar, si desea puede descargar un archivo csv con los diagnósticos.<br>

 
