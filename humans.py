import numpy as np
from settings import HUMANS_DEFAULT_RNG, HUMANS_DEFAULT_N_DIGITS_IN_NAME

NUM_NAME = HUMANS_DEFAULT_N_DIGITS_IN_NAME
rng = np.random.default_rng(HUMANS_DEFAULT_RNG)


class Human:
    def __init__(self, name=None):
        if name is None:
            name = f'Human{rng.integers(1, 10 ** NUM_NAME):0{NUM_NAME}}'
        self.name = name


class Customer(Human):
    def __init__(self, money, name=None):
        if name is None:
            name = f'Customer{rng.integers(1, 10 ** NUM_NAME):0{NUM_NAME}}'
        self.money = money
        super().__init__()
