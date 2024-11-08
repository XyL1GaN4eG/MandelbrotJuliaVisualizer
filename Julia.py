import numpy as np
import matplotlib.pyplot as plt

ROWS, COLS, MAX_ITER = 8000, 8000, 8000  # 2K resolution


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


x_values = np.linspace(-1.5, 1.5, COLS)
y_values = np.linspace(-1.5, 1.5, ROWS)

c = -0.5251993 + 0.5251993j

julia_image = generate_julia_set(x_values, y_values, c)

normed_image = np.log(julia_image + 1)
normed_image = normed_image / np.max(normed_image)

plt.imshow(normed_image, extent=(-1.5, 1.5, -1.5, 1.5), cmap='hot')
plt.axis('off')
plt.savefig('julia_set_8к.png', dpi=300, bbox_inches='tight')
plt.show()
