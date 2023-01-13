import numpy as np
from simpy import Environment
from products import Product
from stocks import Stockpile
from settings import SHOP_DEFAULT_RNG
from processes import customer_generator
import logging

rng = np.random.default_rng(SHOP_DEFAULT_RNG)


class Shop:
    def __init__(self,
                 env: Environment,
                 stockpiles: Stockpile,
                 work_hours=(8, 20),
                 cgenerator=customer_generator()):
        self.work_hours = work_hours
        self.customer_generator = cgenerator
        self.env = env
        self.stockpiles = stockpiles
        self.action = env.process(self.run())
        logging.info('Shop created')

    def run(self):
        while True:
            if self.work_hours[0] <= self.env.now < self.work_hours[1]:
                yield self.env.process(self.sell())
            else:
                yield self.env.process(self.sell())

    def sell(self):
        pass

    def closed(self):
        pass
