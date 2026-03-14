import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50

def build_model_resnet_frozen2(input_shape=(227, 227, 3)):
  base_model = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)
  base_model.trainable = False # Congelamos el 100%

  model = models.Sequential([
      base_model,
      layers.GlobalAveragePooling2D(),
      layers.Dense(1, activation='sigmoid')
  ])
  return model