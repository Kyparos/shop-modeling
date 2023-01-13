import numpy as np
import pandas as pd
from settings import HUMANS_DEFAULT_RNG, HUMANS_DEFAULT_N_DIGITS_IN_NAME

NUM_NAME = HUMANS_DEFAULT_N_DIGITS_IN_NAME
rng = np.random.default_rng(HUMANS_DEFAULT_RNG)


class Human:
    def __init__(self, name=None):
        if name is None:
            name = f'Human{rng.integers(1, 10 ** NUM_NAME):0{NUM_NAME}}'
        self.name = name


class Customer(Human):
    def __init__(self,
                 interest_function=lambda x: rng.exponential(1, x),
                 name=None):
        self.interest_function = interest_function
        if name is None:
            name = f'Customer{rng.integers(1, 10 ** NUM_NAME):0{NUM_NAME}}'
        super().__init__()

    def create_shopping_list(self, products):
        res = pd.DataFrame({'products': products})
        res['amount'] = self.interest_function(len(products))
        res['amount'] = res['amount'].astype(int)
        return res

    def __repr__(self):
        return self.name

