import numpy as np


def uniform(n_rows, n_cols):
    m = np.random.uniform(size=(n_rows, n_cols))
    return m


def gaussian(n_rows, n_cols):
    m = np.random.normal(size=(n_rows, n_cols))
    return m


if __name__ == '__main__':
    print('Gaussian:\n', gaussian(3, 3))
    print('\nUniform:\n', uniform(3, 3))
