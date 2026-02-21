import tensorflow as tf
from tensorflow.keras import layers, models

def build_simple_cnn(input_shape=(227, 227, 3)):
    model = models.Sequential([
        layers.Input(shape=input_shape),
        
        # Una sola capa convolucional
        # Usamos 8 filtros de 3x3 para detectar bordes básicos
        layers.Conv2D(8, (3, 3), activation='relu', padding='same'),
        
        # Global Average Pooling: Reduce cada mapa de activación a un solo número
        layers.GlobalAveragePooling2D(),
        
        # Capa de salida: 1 neurona para clasificación binaria
        layers.Dense(1, activation='sigmoid')
    ])
    return model