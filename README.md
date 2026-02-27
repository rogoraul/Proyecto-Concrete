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

Se utiliza el dataset estándar **Concrete Crack Images for Classification** (Özgenel), disponible en Mendeley Data y Kaggle.
* **Tamaño:** 40.000 imágenes (20.000 Positivas y 20.000 Negativas).
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
│   └── 03_Modelos_Complejos.ipynb 
├── src/                   # Scripts auxiliares
├── models/                # Pesos guardados (.h5)
├── requirements.txt       # Dependencias
└── README.md              # Documentación
```

## 6. Tabla de Resultados

| Modelo | Tipo | Nº Parámetros | Accuracy | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- |:--- |
| Modelo lineal | Regresión Logística | 510 | 98% | 98% | 98% |
| Modelo Machine Learning | Support Vector Machine| 510 | 98% | 98% | 98% |
| Modelo Simple Red Neuronal |  |  |  |  |  |
| Modelo Complejo Red Neuronal |  |  |  |  |  |


## 7. Conclusiones y Próximos Pasos

Como se puede ver en la tabla de resultados, hemos logrado solucionar de manera sobresaliente el problema propuesto de detección de grietas empleando métodos muy eficientes y con baja complejidad computacional. 

**Explicación de Modelos Obtenidos:**
- **Regresión Logística:** Nos entrega probabilidades sobre la pertenencia a una clase. Para este modelo utilizamos la función de coste de **entropía cruzada** (Log Loss) porque penaliza exponencialmente las predicciones que son muy seguras y erróneas, optimizando la capacidad de clasificación probabilística. Hemos aplicado 3 modelos, uno sin preprocesamiento con un accuracy en Test del 90% y 4097 parámetros, uno aplicando HOG con un accuracy en Test del 94% y 1765 parámetros, y uno con HOG y PCA con un accuracy en Test del 98% y 510 parámetros
- **Support Vector Machine (LinearSVC):** Este modelo encuentra el hiperplano óptimo que separa ambas clases. Utiliza como función de coste el **Hinge Loss** dado que su principal objetivo es maximizar el margen que separa las imágenes que tienen grieta de las que no, demostrando ser extremadamente robusto. Hemos aplicado 3 modelos, uno sin preprocesamiento con un accuracy en Test del 88% y 4097 parámetros, uno aplicando HOG con un accuracy en Test del 97.5% y 1765 parámetros, y uno con HOG y PCA con un accuracy en Test del 97.7% y 510 parámetros
- **Red Convolucional**

**Cambio de Objetivo:**
Dado que SVM y la Regresión Logística han logrado solucionar el problema a un nivel casi perfecto (98% de Recall), aplicar y ajustar **Redes Neuronales Convolucionales (CNN) más complejas** sobre este dataset es innecesario, ya que el espacio de mejora es virtualmente inexistente. 

Por tanto, no hay necesidad de usar modelos de Aprendizaje Profundo más profundos para esta versión exacta del problema y el siguiente paso sería cambiar el objetivo del trabajo hacia un entorno más complejo y realista, introduciendo por ejemplo: "estimación volumétrica de la grieta, superficies con distintas texturas o de otros materiales ruidosos..."




