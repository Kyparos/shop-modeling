import numpy as np
from settings import PROCCESSES_DEFAULT_RNG
from humans import Customer

rng = np.random.default_rng(PROCCESSES_DEFAULT_RNG)


def poisson(lambda_=1):
    eps = lambda : rng.exponential(1/lambda_)
    S = eps()
    s_i = 1
    i = 1
    yield 0
    while True:
        if i <= S:
            yield s_i
            i += 1
        else:
            S += eps()
            s_i += 1


def customer_generator(process=poisson(), customer_class=Customer):
    total = 0
    for p in process:
        yield [customer_class() for i in range(p-total)]
        total += p
