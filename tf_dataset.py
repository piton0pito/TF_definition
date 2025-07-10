import os.path

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import pathlib

from config import img_height, img_width, batch_size, output_folder, input_folder, seed

# Определяем директорию с набором данных
if os.path.isdir(output_folder):
    dataset_dir = pathlib.Path(output_folder)
else:
    dataset_dir = pathlib.Path(input_folder)

dataset_dir = pathlib.Path(dataset_dir).with_suffix('')

# Определяем поддерживаемые форматы изображений
supported_formats = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

# Фильтруем директорию набора данных, чтобы включить только поддерживаемые файлы изображений
image_files = [f for f in dataset_dir.glob('*/*') if f.suffix in supported_formats]

# Подсчитываем количество изображений
image_count = len(image_files)
# print(f'Всего изображений: {image_count}')

# Загружаем обучающий набор данных
train_ds = tf.keras.utils.image_dataset_from_directory(
    dataset_dir,
    validation_split=0.2,
    subset='training',
    seed=seed,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

# Загружаем валидационный набор данных
validation_ds = tf.keras.utils.image_dataset_from_directory(
    dataset_dir,
    validation_split=0.2,
    subset='validation',
    seed=seed,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

class_names = train_ds.class_names
# print(f'Class names: {class_names}')

# Кэширование и предварительная выборка
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
validation_ds = validation_ds.cache().prefetch(buffer_size=AUTOTUNE)

if __name__ == "__main__":
    print(f'Всего изображений: {image_count}')
    print(f'Class names: {class_names}')
