import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import sys

import numpy as np
import tensorflow as tf

from config import img_height, img_width, model_name, MAIN, ADDITIONAL, RESET
from tf_dataset import class_names
from tf_model import model

# Загрузка весов
model.load_weights(model_name)

if len(sys.argv) != 3 or sys.argv[1] != '-p':
    print("Usage: ./tf_definition.py -p <path to image>")
    sys.exit(1)

img_path = sys.argv[2]

# Загрузка изображения
img = tf.keras.utils.load_img(img_path, target_size=(img_height, img_width))
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

# Прогноз
prediction = model.predict(img_array)
score = tf.nn.softmax(prediction[0])

print(f"{MAIN}На изображении скорее всего {ADDITIONAL}{class_names[np.argmax(score)]}{MAIN} ({100 * np.max(score):.2f}% вероятность){RESET}")
input("Нажмите Enter, чтобы выйти...")
