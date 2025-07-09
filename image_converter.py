import os
import pathlib

from PIL import Image

from config import input_folder, output_folder
from progress_bar import ProgressBar


def count_total_images(folder):
    """Подсчитывает общее количество PNG изображений во всех подпапках"""
    total = 0
    for subfolder in os.listdir(folder):
        subfolder_path = os.path.join(folder, subfolder)
        if os.path.isdir(subfolder_path):
            total += len([f for f in os.listdir(subfolder_path)])
    return total


def process_images(input_folder, output_folder):
    # Проверяем и создаем выходную папку при необходимости
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Инициализируем прогресс-бар
    total_images = count_total_images(input_folder)
    progress = ProgressBar(
        total=total_images,
        prefix='Обработка изображений:',
        suffix='Выполнено',
        length=30
    )
    print(f"Найдено изображений для обработки: {total_images}")

    # Проходим по всем подпапкам в входной папке
    for subfolder in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder)

        # Проверяем, что это папка
        if os.path.isdir(subfolder_path):
            # Получаем список PNG файлов в подпапке
            png_files = [f for f in os.listdir(subfolder_path)]

            # Обрабатываем каждый PNG файл
            for i, png_file in enumerate(png_files, start=1):
                try:
                    # Формируем пути к файлам
                    input_path = os.path.join(subfolder_path, png_file)
                    output_filename = f"{subfolder}_{i}.jpg"
                    output_path = os.path.join(output_folder, output_filename)

                    # Открываем изображение, конвертируем в ч/б и сохраняем как JPG
                    with Image.open(input_path) as img:
                        bw_img = img.convert('L')
                        bw_img.save(output_path, 'JPEG', quality=95)

                    # Обновляем прогресс-бар
                    progress.update(1)

                except Exception as e:
                    print(f"\nОшибка при обработке {input_path}: {str(e)}")
                    continue

    # Завершаем прогресс-бар
    progress.complete()
    print("\nВсе изображения обработаны!")


if __name__ == "__main__":
    process_images(input_folder, output_folder)
