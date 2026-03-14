# Proyecto: Detección Automática de Grietas en Hormigón 

**Asignatura:** Aprendizaje Profundo 
**Grado:** Ciencia de Datos
**Curso:** 2025/2026

## 1. Descripción del Problema

El hormigón es uno de los materiales más utilizados en la infraestructura civil, y el deterioro de estas estructuras se manifesta normalmente a través de las grietas, las cuales, si no se detectan a tiempo pueden causar problemas en la seguridad estructural. Tradicionalmente, la inspección de estas estructuras se realizaba de forma manual, pero es un proceso muy lento, subjetivo y costoso. Por tanto, este proyecto tiene como objetivo clasificar de forma automática las imágenes de hormigón para detectar fallos estructurales. El problema es una clasificación binaria:
- Clase `1` (Positive): Con Grieta.
- Clase `0` (Negative): Sin Grieta.

Para lograr el objetivo, se va a desarrollar y comparar diferentes arquitecturas de aprendizaje profundo para automatizar la inspección visual en las infraestructuras civiles.

## 2. Dataset

Anteriormente, se había utilizado el dataset estándar **Concrete Crack Images for Classification** (Özgenel), disponible en Mendeley Data y Kaggle, con un tamaño de 40.000 imágenes (20.000 Positivas y 20.000 Negativas).
Pero debido a la simplicidad del problema y de la base de datos, se ha buscado una más compleja, para ello, se ha utilizado el conjunto de datos SDNET2018 del campus de la Universidad Estatal de Utah, Logan, Estados Unidos:
* **Tamaño:** 56.092 imágenes (8.484 Positivas y 47.608 Negativas).
* **Formato:** Imágenes RGB de 227x227 píxeles.
* **Preprocesamiento:** Se realizará una división de los datos (Train/Validation/Test) para asegurar la generalización de los modelos.


## 3. Estado del Arte
La detección de grietas en hormigón ha evolucionado a lo largo de los años, desde el procesamiento de imagen clásido hasta el uso de CNNs. A continuación, se comparan los modelos más relevantes de la literatura aplicados a este problema de la clasificación automática de grietas en hormigón. 

| Modelo / Arquitectura | Año | Dataset | Metricas | Referencia |
| :--- | :--- | :--- | :--- | :--- |
| **ConvNet** | 2016 | 500 imagenes | F1: 89.6%, Recall: 92.5% | Zhang et al. [1] |
| **CNN** (ventana deslizante) | 2017 | 40.000 imagenes | Accuracy: 97.9% | Cha et al. [2] |
| **VGG16** (Transfer) | 2018 | 3500 imagenes | Accuracy: 92.27% | Silva & Lucena [3] |
| **GoogleNet / VGG19/ VGG16** | 2018 | 40.000 imagenes Dataset Mendeley| Accuracy: 99.9% | **Özgenel [4]** |
| **Lightweight CNN** | 2025 | 40.000 imagenes Dataset Mendeley | **98.1%** | **Arici [5]** |

### Referencias Bibliográficas

* **[1]** Zhang, Lei & Yang, Fan & Zhang, Yimin & Zhu, Ying. (2016). Road crack detection using deep convolutional neural network. 10.1109/ICIP.2016.7533052.
  
* **[2]** Cha, Youngjin & Choi, Wooram & Buyukozturk, Oral. (2017). Deep Learning-Based Crack Damage Detection Using Convolutional Neural Networks. Computer-Aided Civil and Infrastructure Engineering. 32. 361-378. 10.1111/mice.12263.
  
* **[3]** Silva, Wilson & Schwerz de Lucena, Diogo. (2018). Concrete Cracks Detection Based on Deep Learning Image Classification. Proceedings. 2. 5387. 10.3390/ICEM18-05387.
  
* **[4]** Özgenel, Çağlar & Sorguc, Arzu. (2018). Performance Comparison of Pretrained Convolutional Neural Networks on Crack Detection in Buildings. 10.22260/ISARC2018/0094.
  
* **[5]** Arici, Ayşe. (2025). Automatic Crack Detection on Concrete Surfaces Using Lightweight Deep Learning Models. Journal of Clinical Case Studies Reviews & Reports. 1-8. 10.47363/JCCSR/2025(7)364.
  
## 4. Métricas de Evaluación 
Para este proyecto se utilizarán las siguientes métricas, priorizando el **Recall**, dado que en ingeniería civil un Falso Negativo (no detectar una grieta real) es el error más grave y peligroso, porque pone en riesgo la seguridad estructural.

* **Nº Parámetros:** Complejidad computacional del modelo.
* **Accuracy:** Precisión global.
* **Recall (Sensibilidad):** Capacidad de encontrar todas las grietas reales.
* **F1-Score:** Equilibrio entre Precision y Recall.

## 5. Estructura del Proyecto
```text
/
├── data/                  # Dataset (no incluido en repositorio por el tamaño)
├── notebooks/
│   ├── 01_EDA_Carga.ipynb       
│   ├── 02_Modelo_Lineal.ipynb
│   ├── 02_Modelo_Machine_Learning.ipynb
│   ├── 02_Modelo_Red_Neuronal_Simple.ipynb  
│   └── 03_Modelos_Complejos_1.ipynb
│   └── 03_Modelos_Complejos_2.ipynb
│   └── 03_Modelos_Complejos_3.ipynb
│   └── 03_Modelos_Complejos_4.ipynb
│   └── 03_Modelos_Complejos_5.ipynb
│   └── 03_Modelos_Complejos_6.ipynb 
├── src/                   # Scripts auxiliares
├── models/                # Pesos guardados (.h5)
├── requirements.txt       # Dependencias
└── README.md              # Documentación
```

## 6. Tabla de Resultados

| Modelo | Tipo | Nº Parámetros | Accuracy | Recall | AUC |
| :--- | :--- | :--- | :--- | :--- |:--- |
| Modelo lineal | Regresión Logística | 510 | Train: %, Val: %, Test: %| Test: % | Test: % |
| Modelo Machine Learning | Support Vector Machine| 510 | Train: %, Val: %, Test: % | Test: % | Test: % |
| Modelo Simple Red Neuronal | CNN | 233 | Train: %, Val: %, Test: % | Train: %, Val: %, Test: % | Train: %, Val: %, Test: % |
| Modelo Complejo 1 | CNN | 23.850.113 | Train: 99.9%, Val: 92.6%, Test: 92.8% | Train: 99.9%, Val: 67.8%, Test: 67.3% | Train: 1.00, Val: 0.863, Test: 0.875|
| Modelo Complejo 2 | CNN | 24.637.313 | Train: 87.5%, Val: 88.6%, Test: 89.5% | Train: 82.3%, Val: 73.0%, Test: 75.1% | Train: 0.934, Val: 0.907, Test: 0.918 |
| Modelo Complejo 3 | CNN | 23.850.113 | Train: 86.0%, Val: 87.1%, Test: 87.9% | Train: 79.8%, Val: 73.8%, Test: 76.5% | Train: 0.919, Val: 0.901, Test: 0.911 |
| Modelo Complejo 4 | CNN | 23.589.761 | Train: 83.1%, Val: 83.7%, Test: 84.2% | Train: 74.0%, Val: 71.1%, Test: 73.5% | Train: 0.878, Val: 0.868, Test: 0.878 |
| Modelo Complejo 5 | CNN | 8.590.209 | Train: 79.6%, Val: 82.0%, Test: 82.3% | Train: 72.7%, Val: 67.4%, Test: 68.3% | Train: 0.843, Val: 0.836, Test: 0.846 |
| Modelo Complejo 6 | CNN | 1.460.609 | Train: 57.2%, Val: 62.0%, Test: 62.4% | Train: 71.9%, Val: 64.9%, Test: 70.8% | Train: 0.698, Val: 0.693, Test: 0.723 |

## 7. Conclusiones y Próximos Pasos

**Explicación de Modelos Obtenidos:**
- **Regresión Logística:** Nos entrega probabilidades sobre la pertenencia a una clase. Para este modelo utilizamos la función de coste de **entropía cruzada** (Log Loss) porque penaliza exponencialmente las predicciones que son muy seguras y erróneas, optimizando la capacidad de clasificación probabilística. Hemos aplicado 3 modelos, uno sin preprocesamiento con un accuracy en Test del 90% y 4097 parámetros, uno aplicando HOG con un accuracy en Test del 94% y 1765 parámetros, y uno con HOG y PCA con un accuracy en Test del 98% y 510 parámetros
- **Support Vector Machine (LinearSVC):** Este modelo encuentra el hiperplano óptimo que separa ambas clases. Utiliza como función de coste el **Hinge Loss** dado que su principal objetivo es maximizar el margen que separa las imágenes que tienen grieta de las que no, demostrando ser extremadamente robusto. Hemos aplicado 3 modelos, uno sin preprocesamiento con un accuracy en Test del 88% y 4097 parámetros, uno aplicando HOG con un accuracy en Test del 97.5% y 1765 parámetros, y uno con HOG y PCA con un accuracy en Test del 97.7% y 510 parámetros
- **Red Neuronal Convolucional:** Se ha diseñado una arquitectura de Red Neuronal Convolucional (CNN) muy simple, compuesta por una capa convolucional de 8 filtros con un kernel de tamaño (3x3) para extraer características básicas de la imagen como bordes y texturas, luego se ha añadido una capa de Global Average Pooling 2D para reducir la dimensionalidad, finalizando con una capa de salida de una neurona con activación sigmoide para la clasificación binaria (Grieta/sano). Durante el entrenamiento, se ha utilizado la funcionalidad de ModelCheckpoint para poder monitorizar la pérdida de validación y guardar los pesos de la mejor época con el mínimo error 'val_loss'. El modelo se ha entrenado durante 120 épocas, aunque la capacidad de computación ha limitado el proceso (se podría haber entrenado con más épocas), ya que al visualizar las curvas de pérdida se puede ver que tanto la línea de entrenamiento como la de validación mantienen una tendencia descendiente, lo que sugiere que el modelo podría seguir mejorando con más épocas de entrenamiento. La curva de pérdida de validación desciende suavemente junto a la de entrenamiento, estabilizandose sin mostrar signos siginficativos de sobreentrenamiento. A parte, el modelo alcanza rapidamente una alta precisión en validación, manteniéndose más o menos alineado con el set de entrenamiento, lo que indica una buena capacidad de generalización.
Al igual que en la regresión logística, se utiliza la entropía cruzada binaria como función de coste para optimizar la probabilidad de acierto del modelo. Se ha logrado un Accuracy del 94% con tan solo 233 parámetros. Mediante la visualización de los mapas de características, se ha validado que la red aprende de sus propios filtros de detección de bordes y texturas, ignorando el ruido del hormigón mejor que los descriptores estáticos como el HOG.

- **CNN compleja 1:** Para el modelo más complejo, se ha hecho fine tuning con una ResNet50. Para ello, se ha añadido una capa densa de 128 neuronas, y se ha modificado los pesos del bloque 5 de la ResNet50.
- **CNN compleja 2:** Se ha congelado el 100% de la ResNet50, reduciendo los parámetros ebtrenables y se ha añadido una capa densa de 512 neuronas.
- **CNN compleja 3:** Manteniendo las ResNet50 congelada, se ha reducido la capa densa oculta de 512 neuronas a solo 128 neuronas, simplificando de esta manera poco a poco el modelo.
- **CNN compleja 4:** Se ha eliminado la capa densa oculta de 128 neuronas y la regularización (el dropout), pasando directamente de la ResNet50 congelada a la unica neurona final de clasificación.
- **CNN compleja 5:** Como ya no quedan capas densas que quitar en la cabeza del modelo, lo que se ha hecho para simplificarlo es quitar capas de la propia red base de la ResNet50, eliminando todo el bloque 5, por tanto ahora el modelo extrae caracteristicas menos profundas y es más pequeño.
- **CNN compleja 6:** Para simplificar aún más la arquitectura, se han eliminado los bloques 4 y 5 de la ResNet50, dejando únicamente las capas de extracción de texturas y bordes básicos.

Se puede observar que el modelo de la CNN compleja 1, ha logrado memorizar el conjunto de entrenamiento de forma casi perfecta (Accyracy y Recall del 99.9%, AUC de 1.00). Sin embargo, al evaluarlo en validación y test, las metricas han caído drasticamente, con un recall aproximadamente del 67%, demostrando claramente un problema de sobreajuste, debido al exceso de capacidad de aprendizaje al haber descongelado el bloque 5. 
Por otro lado, el modelo de la CNN compleja 6 (que es el más simplificado del modelo complejo inicial), no ha tenido capacidad suficiente para aprender los patrones de las grietas, presentando un accuracy del 57% en entrenamiento y un AUC de 0.698, lo que muestra un problema de underfitting debido al alto bias.
Por último, los modelos 2 y 3 de la CNN compleja representan el equilibrio ideal para este problema de clasificación de grietas. Al mantener la ResNet50 congelada actuando como un extractor de caracteristicas muy potente, y combinarlo con una cabeza densa moderada de unas 512 neuronas o 128 neuronas, el modelo logra la mejor capacidad de generalización. El modelo 2 alcanza un AUC en Test de 0.918, un Accuracy de 89.5% y un Recall de 75.1%, demostrando ser el más robusto y fiable para nuetsro problema de detección de grietas sin caer en el riesgo de la memorización de los datos de entrenamiento. 




