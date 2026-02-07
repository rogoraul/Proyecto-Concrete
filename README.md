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
La detección automática de grietas en hormigón ha sido ampliamente estudiada en la última década. A continuación, se presenta un análisis de los modelos más relevantes aplicados a este problema, contrastando arquitecturas diseñadas desde cero frente a estrategias de Transfer Learning.

| Modelo / Arquitectura | Año | Dataset | Metricas | Referencia |
| :--- | :--- | :--- | :--- | :--- |
| **ConvNet** | 2016 | 500 imagenes | F1: 89.6%, Recall: 92.5% | Zhang et al. [1] |
| **CNN** con ventana deslizante | 2017 | 322 imagenes | Accuracy: 97.9% | Cha et al. [2] |
| **VGG16 (Transfer)** | 2018 | 3500 imagenes | Accuracy: 92.27% | Silva & Lucena [3] |
| **GoogleNet / VGG19/ VGG16** | 2018 | 40.000 imagenes | Accuracy: ~0,98% | **Özgenel [4]** |
| **Lightweight CNN** | 2025 | 40.000 imagenes | **98.1%** | **Arici [5]** |

### Referencias Bibliográficas

* **[1]** Zhang, Lei & Yang, Fan & Zhang, Yimin & Zhu, Ying. (2016). Road crack detection using deep convolutional neural network. 10.1109/ICIP.2016.7533052.
  
* **[2]** Cha, Youngjin & Choi, Wooram & Buyukozturk, Oral. (2017). Deep Learning-Based Crack Damage Detection Using Convolutional Neural Networks. Computer-Aided Civil and Infrastructure Engineering. 32. 361-378. 10.1111/mice.12263.
  
* **[3]** Silva, Wilson & Schwerz de Lucena, Diogo. (2018). Concrete Cracks Detection Based on Deep Learning Image Classification. Proceedings. 2. 5387. 10.3390/ICEM18-05387.
  
* **[4]** Özgenel, Çağlar & Sorguc, Arzu. (2018). Performance Comparison of Pretrained Convolutional Neural Networks on Crack Detection in Buildings. 10.22260/ISARC2018/0094.
  
* **[5]** Arici, Ayşe. (2025). Automatic Crack Detection on Concrete Surfaces Using Lightweight Deep Learning Models. Journal of Clinical Case Studies Reviews & Reports. 1-8. 10.47363/JCCSR/2025(7)364.
  
### Métricas de Evaluación Seleccionadas
Para este proyecto se utilizarán las siguientes métricas, priorizando el **Recall**, dado que en ingeniería civil un Falso Negativo (no detectar una grieta real) es el error más grave y peligroso.

* **Accuracy:** Precisión global.
* **Recall (Sensibilidad):** Capacidad de encontrar todas las grietas reales.
* **F1-Score:** Equilibrio entre Precision y Recall.
* **Nº Parámetros:** Complejidad computacional del modelo.


