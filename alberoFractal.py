import numpy as np
import matplotlib.pyplot as plt

# Параметры изображения
WIDTH, HEIGHT = 800, 800
MAX_ITER = 100

# Функция для вычисления фрактала де Альберо
def albero_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    # Создаем массив для хранения значений
    image = np.zeros((height, width))

    # Генерируем координаты для каждого пикселя
    for x in range(width):
        for y in range(height):
            # Преобразуем пиксельные координаты в комплексные числа
            zx = np.linspace(xmin, xmax, width)[x]
            zy = np.linspace(ymin, ymax, height)[y]
            z = complex(zx, zy)

            # Начальное значение
            c = z
            n = 0

            # Итерации
            while abs(z) < 2 and n < max_iter:
                z = z**3 + c  # Изменяем степень на 3 для фрактала де Альберо
                n += 1

            # Записываем количество итераций в массив
            image[y, x] = n

    return image

# Параметры области отображения
xmin, xmax = -1.5, 1.5
ymin, ymax = -1.5, 1.5

# Генерация фрактала
fractal_image = albero_fractal(xmin, xmax, ymin, ymax, WIDTH, HEIGHT, MAX_ITER)

# Нормализация значений для улучшения визуализации
normed_image = np.log(fractal_image + 1)  # Логарифмическая нормализация
normed_image = normed_image / np.max(normed_image)  # Нормализация к диапазону [0, 1]

# Визуализация
plt.figure(figsize=(10, 10))
plt.imshow(normed_image, extent=(xmin, xmax, ymin, ymax), cmap='hot')  # Используем cmap='hot' для ярких цветов
# plt.colorbar()
# plt.title("Фрактал де Альберо")
plt.axis('off')
plt.savefig("albero", dpi=300, bbox_inches='tight')
plt.show()