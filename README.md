# Proyecto: Detección Automática de Grietas en Hormigón 

**Asignatura:** Aprendizaje Profundo 

## 1. Descripción del Problema

El hormigón es uno de los materiales más utilizados en la infraestructura civil, y el deterioro de estas estructuras se manifesta normalmente a través de las grietas, las cuales, si no se detectan a tiempo pueden causar problemas en la seguridad estructural. Tradicionalmente, la inspección de estas estructuras se realizaba de forma manual, pero es un proceso muy lento, subjetivo y costoso. Por tanto, este proyecto tiene como objetivo clasificar de forma automática las imágenes de hormigón para detectar fallos estructurales. El problema es una clasificación binaria:
- `1`: Positive (Grieta).
- `0`: Negative (Sin Grieta).

Para lograr el objetivo, se va a desarrollar y comparar diferentes arquitecturas de aprendizaje automático y profundo para automatizar la inspección visual en las infraestructuras civiles.

## 2. Dataset

Se utiliza el dataset **Concrete Crack Images for Classification**, disponible a través de Kaggle.
* **Tamaño:** 40.000 imágenes (20.000 Positivas y 20.000 Negativas).
* **Formato:** Imágenes RGB de 227x227 píxeles.
* **División:** Se realizará un split de Train/Validation/Test para la generalización de los modelos.


## 3. Estado del Arte
La detección automática de grietas en hormigón ha sido ampliamente estudiada en la última década. A continuación, se presenta un análisis de los modelos más relevantes aplicados a este problema, contrastando arquitecturas diseñadas desde cero (Custom CNN) frente a estrategias de Transfer Learning.
Es importante notar que, para el dataset específico utilizado en este proyecto (imágenes de 227x227 sin fondo complejo), la literatura reporta precisiones muy altas, situando el estado del arte por encima del 98%.

| Modelo / Arquitectura | Año | Técnica Principal | Metricas | Fuente / Referencia |
| :--- | :--- | :--- | :--- | :--- |
|Custom ConvNet | 2016 | CNN Propia (Supervisado) | F1: 89.6%, AUC: 0.96, Recall: 92.5%, Precision: 86.9% | Zhang et al. [1] |
|CNN (Sliding Window) | 2017 | CNN con Ventana Deslizante | Accuracy: 97.9% | Cha et al. [2] |
|VGG16 (Pre-trained) | 2018 | Transfer Learning (ImageNet) | 99.8% | Silva & Lucena [3] |
|ResNet-50 / VGG19 | 2019 | Comparativa Transfer Learning | 99.9% | Özgenel (Autor del Dataset) [4] |
|MobileNet | 2020 | CNN Ligera (Dispositivos Móviles) | 99.1% | D.J. Kim et al. [5] |
|VGG16 (Modificado) | 2021 | Semantic Segmentation (FCN) | 98.7% (F1) | H.W. Golding et al. [6] |

### Referencias Bibliográficas
[1] Zhang, L., et al. (2016). "Road crack detection using deep convolutional neural network". IEEE International Conference on Image Processing (ICIP).
[2] Cha, Y.J., et al. (2017). "Deep learning-based crack damage detection using convolutional neural networks". Computer-Aided Civil and Infrastructure Engineering.
[3] Silva, W.R., & Lucena, D.S. (2018). "Concrete Cracks Detection Based on Deep Learning Image Classification". Proceedings of the XVIII International Conference on Structural Health Monitoring.
[4] Özgenel, Ç.F. (2019). "Performance Comparison of Pre-Trained Convolutional Neural Networks for Concrete Crack Detection". International Conference on Artificial Intelligence and Data Processing (IDAP).
[5] Kim, D.J., et al. (2020). "Concrete crack detection with light-weight deep learning models". Journal of Computing in Civil Engineering.
[6] Golding, H.W., et al. (2021). "A deep learning based approach for crack detection in concrete images". Structural Health Monitoring.

### Métricas de Evaluación Seleccionadas
Para este proyecto se reportarán las siguientes métricas, priorizando el **Recall**, dado que en ingeniería civil un Falso Negativo (no detectar una grieta real) es el error más peligroso.

* **Accuracy:** Precisión global.
* **Recall (Sensibilidad):** Capacidad de encontrar todas las grietas reales.
* **F1-Score:** Equilibrio entre Precision y Recall.
* **Nº Parámetros:** Complejidad computacional del modelo.


