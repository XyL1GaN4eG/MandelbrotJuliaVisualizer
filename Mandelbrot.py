import numpy as np
import matplotlib.pyplot as plt
import os

ROWS, COLS, MAX_ITER = 800, 800, 1500  # Установлено фиксированное количество итераций

def mandelbrot(c):
    z = 0
    for n in range(MAX_ITER):
        if abs(z) > 4:
            return n
        z = z ** 2 + c
    return MAX_ITER

def generate_mandelbrot_set(x_range, y_range):
    m_set = np.zeros((len(x_range), len(y_range)))
    for i, x in enumerate(x_range):
        for j, y in enumerate(y_range):
            c = complex(x, y)
            m_set[i, j] = mandelbrot(c)
    return m_set

# Создаем папку для сохранения изображений, если она не существует
output_dir = 'mandelbrot'
os.makedirs(output_dir, exist_ok=True)

# Задаем набор значений c
c_values = [
    complex(-0.7, 0.27015),
    complex(-0.4, 0.6),
    complex(0.355, 0.355),
    complex(0.0, 0.0),
    complex(0.3, 0.5)
]

# Генерация изображений для каждого значения c
for c in c_values:
    x_values = np.linspace(-2, 1, COLS)  # Изменено на COLS для правильного отображения
    y_values = np.linspace(-1, 1, ROWS)  # Изменено на ROWS для правильного отображения

    mandelbrot_image = generate_mandelbrot_set(x_values, y_values)

    # Нормализация значений для более плавного перехода
    normed_image = np.log(mandelbrot_image + 1)  # Логарифмическая нормализация
    normed_image = normed_image / np.max(normed_image)  # Нормализация в диапазоне [0, 1]

    plt.imshow(normed_image.T, cmap='inferno', extent=[-2, 1, -1, 1])
    plt.axis("off")
    plt.title(f'Mandelbrot Set for c = {c}')
    plt.savefig(os.path.join(output_dir, f'mandelbrot_set_c_{c.real:.3f}_{c.imag:.3f}.png'), dpi=300, bbox_inches='tight')
    plt.close()  # Закрываем текущее изображение, чтобы избежать наложения