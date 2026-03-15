import tensorflow as tf
from tensorflow.keras import layers, models
def build_simple_2(input_shape=(227, 227, 3)):
  model = models.Sequential([
          layers.Input(shape=input_shape),

          layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
          layers.MaxPooling2D((2, 2)),
          layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
          layers.MaxPooling2D((2, 2)),
          layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
          layers.MaxPooling2D((2, 2)),

          layers.GlobalAveragePooling2D(),
          layers.Dense(256, activation='relu'),
          layers.Dropout(0.3),
          layers.Dense(1, activation='sigmoid')
      ])
  return model