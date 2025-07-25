import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import matplotlib.pyplot as plt

from config import epochs, model_name
from tf_dataset import train_ds, validation_ds
from tf_model import model

history = model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=epochs,
)
# Визуализация результатов обучения и валидации
acc = history.history['accuracy']
validation_acc = history.history['val_accuracy']
loss = history.history['loss']
validation_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Точность обучения')
plt.plot(epochs_range, validation_acc, label='Точность валидации')
plt.legend(loc='lower right')
plt.title('Точность обучения и валидации')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Тренировочные потери')
plt.plot(epochs_range, validation_loss, label='Валидационные потери')
plt.legend(loc='upper right')
plt.title('Потеря обучения и валидации')
plt.show()

# Сохранение всей модели
model.save(model_name)
print("Модель сохранена")
