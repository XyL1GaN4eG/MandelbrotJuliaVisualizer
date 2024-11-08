import numpy as np
import matplotlib.pyplot as plt

ROWS, COLS, MAX_ITER = 800, 800, 2000


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


x_values = np.linspace(-2, 1, ROWS)
y_values = np.linspace(-1, 1, COLS)

mandelbrot_image = generate_mandelbrot_set(x_values, y_values)

# Нормализация значений для более плавного перехода
normed_image = np.log(mandelbrot_image + 1)  # Логарифмическая нормализация
normed_image = normed_image / np.max(normed_image)  # Нормализация в диапазоне [0, 1]

plt.imshow(normed_image.T, cmap='inferno', extent=[-2, 1, -1, 1])
plt.axis("off")
plt.savefig('mandelbrot_set.png', dpi=300, bbox_inches='tight')
