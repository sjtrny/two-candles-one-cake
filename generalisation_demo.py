from utils import BetaBD, UniformBD, calculate_prob
from functools import partial

Beta22 = partial(BetaBD, a=2, b=2)

p = calculate_prob(Beta22, UniformBD, UniformBD)

print(p)
