import numpy as np
from products import Product
from settings import STOCKS_DEFAULT_RNG, STOCKS_DEFAULT_N_DIGITS_IN_NAME

NUM_NAME = STOCKS_DEFAULT_N_DIGITS_IN_NAME
rng = np.random.default_rng(STOCKS_DEFAULT_RNG)


class Stockpile:
    def __init__(self, capacity, contains=None, name=None):
        if contains is None:
            contains = []
        self.name = name if name is not None else f'Stockpile{rng.integers(1, 10 ** NUM_NAME):0{NUM_NAME}}'
        self.capacity = capacity
        self.contains = contains
        self.is_visitor_accessible = False

    def get_taken_space(self):
        return sum(list(map(lambda x: x.size, self.contains)))

    def get_free_space(self):
        return self.capacity - self.get_taken_space()

    def product_fits(self, product: Product):
        return product.amount < self.get_free_space()


class DedicatedStockpile(Stockpile):
    def __init__(self, capacity, product_types=None, contains=None, name=None):
        super().__init__(capacity, contains, name)
        if product_types is None:
            self.product_types = set()

    def product_fits(self, product: Product):
        condition_1 = product.amount < self.get_free_space()
        condition_2 = len(product.types / self.product_types) == 0
        return condition_1 and condition_2


class Display(Stockpile):
    def __init__(self, capacity, contains=None, name=None):
        super().__init__(capacity, contains=[], name=None)
        self.is_visitor_accessible = True


class DedicatedDisplay(DedicatedStockpile, Display):
    def __init__(self, capacity, product_types=None, contains=None, name=None):
        super().__init__(capacity, product_types, contains, name)
