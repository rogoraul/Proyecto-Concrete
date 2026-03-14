import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model

def build_modelo_resnet_simple(input_shape=(227, 227, 3)):
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)

    # Cortamos la red aún más atrás, al final del bloque 3
    capa_salida = base_model.get_layer('conv3_block4_out').output
    extractor_reducido = Model(inputs=base_model.input, outputs=capa_salida)
    extractor_reducido.trainable = False

    model = models.Sequential([
        extractor_reducido,
        layers.GlobalAveragePooling2D(),
        layers.Dense(1, activation='sigmoid')
    ])
    return model