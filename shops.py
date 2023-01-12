import numpy as np
from simpy import Environment
from products import Product
from stocks import Stockpile
from settings import SHOP_DEFAULT_RNG

rng = np.random.default_rng(SHOP_DEFAULT_RNG)


class Shop:
    def __init__(self,
                 env: Environment,
                 stockpiles: Stockpile,
                 customer_generator=None):  # TODO: implement customer generator
        self.customer_generator = customer_generator
        self.env = env
        self.stockpiles = stockpiles
        self.action = env.process(self.run(env))

    def run(self, env):
        pass  # TODO: implement run
