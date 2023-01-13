import numpy as np
from settings import PRODUCTS_DEFAULT_RNG, PRODUCTS_DEFAULT_N_DIGITS_IN_NAME
import logging

NUM_NAME = PRODUCTS_DEFAULT_N_DIGITS_IN_NAME
rng = np.random.default_rng(PRODUCTS_DEFAULT_RNG)


class Product:

    def __init__(self,  cost, name=None):
        self.name = name if name is not None else f'Product{rng.integers(1, 10 ** NUM_NAME):0{NUM_NAME}}'
        self.cost = cost
        self.types = set()

    def __repr__(self):
        return f'<{self.name} | {self.cost}>'



