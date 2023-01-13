from products import Product
from stocks import Stockpile
from shops import Shop
import pandas as pd
import simpy

if __name__ == '__main__':
    df_stock = pd.DataFrame({'products':[Product(3), Product(4)],
                             'amount': [3, 2]})
    stock_pile = Stockpile(15, contains=df_stock)
    env = simpy.Environment()
    shop = Shop(env, stock_pile)
    env.run(until=24)
