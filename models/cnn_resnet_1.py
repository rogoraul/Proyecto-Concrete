import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50

def build_model_resnet_finetuned(input_shape=(227, 227, 3)):
  base_model = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)
  base_model.trainable = False

  # Descongelamos solo el último bloque
  base_model.trainable = True
  for layer in base_model.layers:
      if layer.name == 'conv5_block1_1_conv':
          break
      layer.trainable = False

  model = models.Sequential([
      base_model,
      layers.GlobalAveragePooling2D(),
      layers.Dense(128, activation='relu'),
      layers.Dropout(0.3),
      layers.Dense(1, activation='sigmoid')
  ])
  return model