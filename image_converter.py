import os
from PIL import Image
from progress_bar import ProgressBar


def count_png_images(root_folder):
    total_images = 0
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith('.png'):
                total_images += 1
    return total_images


def convert_images_to_jpg(root_folder):
    # Инициализируем прогресс-бар
    total_images = count_png_images(root_folder)
    progress = ProgressBar(
        total=total_images,
        prefix='Обработка изображений:',
        suffix='Выполнено',
        length=30
    )

    for foldername, subfolders, filenames in os.walk(root_folder):
        # Получаем имя папки
        folder_name = os.path.basename(foldername)
        # Счетчик для порядкового номера
        counter = 1

        for filename in filenames:
            if filename.lower().endswith('.png'):
                # Полный путь к изображению
                png_image_path = os.path.join(foldername, filename)

                try:
                    # Открываем изображение
                    with Image.open(png_image_path) as img:
                        # Конвертируем в RGB (JPG не поддерживает альфа-канал)
                        rgb_image = img.convert('RGB')

                        # Создаем новое имя файла
                        new_filename = f"{folder_name}_{counter}.jpg"
                        jpg_image_path = os.path.join(foldername, new_filename)

                        # Сохраняем изображение в формате JPG
                        rgb_image.save(jpg_image_path, 'JPEG')

                        # Удаляем исходное PNG изображение
                        os.remove(png_image_path)

                        # Увеличиваем счетчик
                        counter += 1

                        # Обновляем прогресс-бар
                        progress.update(1)

                except Exception as e:
                    print(f"Ошибка при обработке файла {png_image_path}: {e}")

    progress.complete()


# Укажите путь к корневой папке
root_folder = 'D:\\PyCarm Progect\\Sum_practic\\data'

# Считаем количество изображений перед конвертацией
total_images = count_png_images(root_folder)
print(f"Общее количество изображений для конвертации: {total_images}")

# Запускаем конвертацию
convert_images_to_jpg(root_folder)
