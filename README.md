# Proyecto-YUCA

# Proyecto YUCA: Clasificación de Enfermedades en Hojas de Yuca mediante Deep Learning

**Asignatura:** Aprendizaje Profundo (Deep Learning)  
**Entrega:** Fase 1 - Selección del problema, Datos y Estado del Arte  
**Estado:** En desarrollo

## 1. Descripción del Problema

La yuca (Cassava) es la segunda fuente más importante de carbohidratos en África, un cultivo vital para la seguridad alimentaria de más de 500 millones de personas. Sin embargo, el 80% de los cultivos domésticos están amenazados por enfermedades virales que son difíciles de distinguir a simple vista por agricultores no expertos.

El objetivo de este proyecto es desarrollar un modelo de Deep Learning capaz de clasificar imágenes de hojas de yuca en 5 categorías (4 enfermedades y 1 categoría sana) para asistir en la detección temprana de patologías.

El problema presenta desafíos técnicos interesantes para la asignatura:
- **Similitud visual:** Las enfermedades presentan patrones visuales muy parecidos (manchas amarillas/marrones).
- **Desbalanceo de clases:** La clase Cassava Mosaic Disease (CMD) es dominante.
- **Ruido:** Las fotos están tomadas en condiciones de campo reales (iluminación variable, fondos complejos).

## 2. Dataset

Se utilizará el conjunto de datos **Cassava Leaf Disease Classification**, disponible originalmente a través de Kaggle y el Makerere AI Lab.

- **Origen:** Kaggle Competition Dataset
- **Tamaño:** 21,397 imágenes etiquetadas.
- **Resolución:** Imágenes RGB de alta resolución (se redimensionarán para el entrenamiento).
- **Clases (Labels):**
    - `0`: Cassava Bacterial Blight (CBB)
    - `1`: Cassava Brown Streak Disease (CBSD)
    - `2`: Cassava Green Mottle (CGM)
    - `3`: Cassava Mosaic Disease (CMD) — *Clase mayoritaria*
    - `4`: Healthy (Sana)

## 3. Estado del Arte (State of the Art)

A continuación, se presenta un análisis de los modelos más relevantes aplicados a este problema específico, basándonos en la literatura académica reciente y los resultados de la competición internacional.

| Modelo / Arquitectura | Año | Técnica Principal | Accuracy (Validación) | Fuente / Referencia |
| :--- | :--- | :--- | :--- | :--- |
| **ResNet-50** | 2019 | Transfer Learning (Baseline) | 83.4% | Mwebaze et al. (iCassava Paper) [1] |
| **InceptionV3** | 2020 | Multi-scale CNN | 86.2% | Ramcharan et al. [2] |
| **EfficientNet-B3** | 2020 | Scaling Compuesto + Augmentation Pesado | 88.6% | Sambo et al. / Kaggle Kernels [3] |
| **Vision Transformer (ViT)** | 2021 | Self-Attention (Sin Convoluciones) | 89.5% | Winning Solutions Analysis [4] |
| **Ensemble (EffNet + ViT)** | 2021 | Model Ensembling + TTA (Test Time Augmentation) | 90.8% | Kaggle Leaderboard Top 1% [5] |

### Referencias
- [1] Mwebaze et al. (2019). "iCassava 2019 Fine-Grained Visual Categorization Challenge". arXiv:1908.02900.
- [2] Ramcharan, A., et al. (2017/2019). "Deep Learning for Image-Based Cassava Disease Detection". Frontiers in Plant Science.
- [3] Sambo et al. (2020). "Review of Deep Learning for Cassava Disease".
- [4] Dosovitskiy et al. (2020) & Public Notebooks: "ViT on Cassava".
- [5] Kaggle Competition Leaderboard (2021).
