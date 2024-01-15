# Detector_plagas_ml_CNN
## Clasificar e identificar las plagas en cultivos a partir de fotos.
El proyecto utiliza un modelo de Convolutional Neural Network (CNN) para detectar plagas en cultivos a partir de imágenes ingresadas. Estas enfermedades se clasifican en tres categorías: cultivos sanos, cultivos enfermos y cultivos con plagas de artrópodos. La implementación de este modelo tiene diversas ventajas:<br>

- **Detección temprana de enfermedades:**
  El CNN identifica signos tempranos de enfermedades en las plantas, permitiendo a los agricultores tomar medidas preventivas antes de que las enfermedades se propaguen y afecten significativamente los cultivos.<br>

- **Optimización del uso de pesticidas:**
  La identificación precisa de enfermedades permite a los agricultores aplicar tratamientos específicos y oportunos, optimizando así el uso de pesticidas y reduciendo el desperdicio, lo que contribuye a minimizar el impacto ambiental.<br>

- **Aumento de la productividad:**
  La prevención y gestión eficaz de enfermedades aumenta la productividad agrícola al evitar pérdidas significativas de cosechas.<br>

- **Reducción de costos:**
  La detección temprana y gestión precisa de enfermedades ayudan a reducir costos asociados con la pérdida de cultivos y el uso excesivo de pesticidas.<br>

- **Sostenibilidad agrícola:**
  Al minimizar el uso de productos químicos y maximizar la salud de los cultivos, el proyecto promueve prácticas agrícolas sostenibles y respetuosas con el medio ambiente.<br>

- **Facilitación de decisiones:**
  La clasificación automática de enfermedades proporciona información valiosa para que los agricultores tomen decisiones informadas sobre el manejo de los cultivos, la planificación de la cosecha y la gestión de plagas.<br>

- **Acceso a recursos limitados:**
  Permite a los agricultores en regiones con recursos limitados beneficiarse de tecnologías avanzadas para el diagnóstico y gestión eficiente de enfermedades.<br>

- **Educación agrícola:**
  El proyecto sirve como herramienta educativa para agricultores y profesionales agrícolas, ayudándolos a comprender y abordar mejor los problemas de enfermedades en los cultivos.<br>
  
- **Funcionamiento:**
    
![](https://github.com/alvaroOficial/Detector_plagas_ml_CNN/blob/main/0p.png)
  En el proyecto, puedes cargar la cantidad de imágenes que desees de tus cultivos, y el programa devolverá un diagnóstico sobre el tipo de plaga o si la planta está saludable. Solo necesitas presionar "Browse files", seleccionar los archivos y realizar la predicción.

    
![](https://github.com/alvaroOficial/Detector_plagas_ml_CNN/blob/main/0p1.png)
Los resultados se pueden ver en una tabla y tambien en la imagen.Además, tienes la opción de realizar un diagnóstico rápido, que activa la cámara y toma una foto instantánea para proporcionar un diagnóstico.si desea puede descargar un archivo csv con los resultados

  
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
 d)Finalmente seleccione la cantidad y suba las imágenes a detectar,en la carpeta imagenes_evaluacion encontrara varias imagenes que puede usar de prueba.Una vez se hace el diagnostico si desea puede descargar un archivo csv con los resultados.<br>
 
## Conclusiones
Es importante tener en cuenta que resulta útil entrenar primero el archivo y posteriormente tomar ese modelo ya entrenado, pues reduce demasiado el tiempo de procesamiento y permite crear un código mucho más amigable y sencillo por ejemplo en este caso en la interfaz gráfica.<br>
En síntesis, si bien se obtuvo un accuracy entre el 0.88 y el 0.9 en el modelo variando parámetros, se puede decir que la clasificación dentro de las tres clases es bastante buena, sin embargo algo a considerar es que en la sección de insectos, tiende a ocurrir más errores debido a la gran variedad de especies, débil cantidad de datos de entrenamiento.<br>
Por otra parte, resulta útil un proyecto de Convolutional Neural Network (CNN) diseñado para clasificar enfermedades en cultivos ofrece beneficios significativos en la agricultura. Permitiendo la detección temprana de enfermedades, optimizando el uso de pesticidas, aumentando la productividad agrícola y reduciendo costos, contribuye a prácticas agrícolas más sostenibles. Este enfoque eficiente también facilita decisiones informadas para los agricultores, especialmente en áreas con recursos limitados, y sirve como una valiosa herramienta educativa. En resumen, el proyecto mejora la salud de los cultivos, la eficiencia en la gestión agrícola y tiene un impacto positivo en la sostenibilidad y productividad agrícolas.
 
