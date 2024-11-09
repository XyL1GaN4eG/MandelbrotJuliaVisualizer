import numpy as np
import matplotlib.pyplot as plt
import os

# Функция для вычисления числа итераций для точки c
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 4:
            return n
        z = z ** 2 + c
    return max_iter

# Функция для генерации множества Мандельброта
def generate_mandelbrot_set(x_range, y_range, max_iter):
    m_set = np.zeros((len(x_range), len(y_range)))
    for i, x in enumerate(x_range):
        for j, y in enumerate(y_range):
            c = complex(x, y)
            m_set[i, j] = mandelbrot(c, max_iter)
    return m_set

# Создаем папку для сохранения изображений, если она не существует
output_dir = 'mandelbrot'
os.makedirs(output_dir, exist_ok=True)

# Определяем диапазоны и количество итераций
x_values = np.linspace(-2, 1, 800)
y_values = np.linspace(-1, 1, 800)

# Список различных значений максимального числа итераций
max_iters = [100, 300, 500, 1000, 1500]

# Генерация изображений для разных значений max_iter
for max_iter in max_iters:
    mandelbrot_image = generate_mandelbrot_set(x_values, y_values, max_iter)

    # Нормализация значений для более плавного перехода
    normed_image = np.log(mandelbrot_image + 1)  # Логарифмическая нормализация
    normed_image = normed_image / np.max(normed_image)  # Нормализация в диапазоне [0, 1]

    plt.imshow(normed_image.T, cmap='inferno', extent=[-2, 1, -1, 1])
    plt.axis("off")
    plt.title(f'Mandelbrot Set (max_iter={max_iter})')
    plt.savefig(os.path.join(output_dir, f'mandelbrot_set_{max_iter}.png'), dpi=300, bbox_inches='tight')
    plt.close()  # Закрываем текущее изображение, чтобы избежать наложения