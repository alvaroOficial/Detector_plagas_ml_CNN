# Detector_plagas_ml_CNN
## Clasificar e identificar las plagas en cultivos a partir de fotos.
![](https://github.com/alvaroOficial/Detector_plagas_ml_CNN/blob/main/esquema.png)
## EJECUCIÓN
Se tienen dos partes para el código; en la primera parte se entrena el modelo con las imágenes del dataset
 a) Haber instalado las librerías necesarias para redes CNN como tensorflow,keras
 b) Descargar y ubicar correctamente el dataset.<br>
 c) abrir el archivo modelo_entrennamiento.ipynb; reemplazar las rutas y ejecutarlo.
 d) Entrenar el modelo con el dataset y parametros a decisión.
 d) se tendrá como salida dos archivos .h5 con el modelo y sus pesos.

 --------------------------------------------------------------------------------
Para la segunda parte e ejecuta el modelo ya entrenado y se crea el local host:
 se recomienda tener las librerías de streamlit.
 e) Abrir el archivo salida.py
 d) Ubicar correctamente la ruta de modelo.h5 y de pesos.h5
 e) una vez se ejecute correctamente, se debe abrir el local host desde la terminal.
 d)Finalmente seleccione la cantidad y suba las imágenes a detectar, si desea puede descargar un archivo csv con los diagnósticos.

 
