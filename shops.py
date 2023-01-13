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
                 cgenerator=customer_generator(),
                 assortiment=None):
        if assortiment is None:
            assortiment = stockpiles.contains.products
        self.work_hours = work_hours
        self.cgenerator = cgenerator
        self.env = env
        self.stockpiles = stockpiles
        self.action = env.process(self.run())
        self.assortiment = assortiment
        logging.info('Shop created')

    def run(self):
        while True:
            if self.work_hours[0] <= self.env.now < self.work_hours[1]:
                yield self.env.process(self.sell())
            else:
                yield self.env.process(self.closed())

    def sell(self):
        for c in next(self.cgenerator):
            if not c:
                break
            shopping_list = c.create_shopping_list(self.assortiment)
            receipt = self.stockpiles.get(shopping_list)
        yield self.env.timeout(1)

    def closed(self):
        yield self.env.timeout(1)
