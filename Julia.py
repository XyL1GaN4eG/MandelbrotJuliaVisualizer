import numpy as np
import matplotlib.pyplot as plt
import os

ROWS, COLS = 800, 800  # 2K resolution
MAX_ITER = 1500  # Установлено фиксированное количество итераций

def julia(c):
    def mandelbrot(z):
        for n in range(MAX_ITER):
            if abs(z) > 4:
                return n
            z = z ** 2 + c
        return MAX_ITER

    return mandelbrot

def generate_julia_set(x_range, y_range, c):
    j_set = np.zeros((len(x_range), len(y_range)))
    for i, x in enumerate(x_range):
        for j, y in enumerate(y_range):
            z = complex(x, y)
            j_set[i, j] = julia(c)(z)
    return j_set

# Создаем папку для сохранения изображений, если она не существует
output_dir = 'julia'
os.makedirs(output_dir, exist_ok=True)

x_values = np.linspace(-1.5, 1.5, COLS)
y_values = np.linspace(-1.5, 1.5, ROWS)

# Задаем набор значений c
c_values = [
    -0.5251993 + 0.5251993j,
    -0.7 + 0.27015j,
    -0.4 + 0.6j,
    0.355 + 0.355j,
    0.0 + 0.0j
]

# Генерация изображений
for c in c_values:
    julia_image = generate_julia_set(x_values, y_values, c)

    normed_image = np.log(julia_image + 1)
    normed_image = normed_image / np.max(normed_image)

    plt.imshow(normed_image, extent=(-1.5, 1.5, -1.5, 1.5), cmap='hot')
    plt.axis('off')
    plt.title(f'c = {c}')
    plt.savefig(os.path.join(output_dir, f'julia_set_c_{c.real:.3f}_{c.imag:.3f}.png'), dpi=300, bbox_inches='tight')
    plt.close()  # Закрываем текущее изображение, чтобы избежать наложения