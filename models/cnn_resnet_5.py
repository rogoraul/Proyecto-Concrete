import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model

def build_modelo_resnet_bloque(input_shape=(227, 227, 3)):
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)

    # Cortamos la red al final del bloque 4 quitndo todas las capas del bloque 5
    capa_salida = base_model.get_layer('conv4_block6_out').output
    extractor_reducido = Model(inputs=base_model.input, outputs=capa_salida)
    extractor_reducido.trainable = False

    model = models.Sequential([
        extractor_reducido,
        layers.GlobalAveragePooling2D(),
        layers.Dense(1, activation='sigmoid')
    ])
    return model