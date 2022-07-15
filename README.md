# Two Candles, One Cake

# Problem

Given a rectangular and unit length cake, suppose that:
* two candles are placed uniform at random along the length
* a knife cuts the cake at a uniform random position along the length

**What is the probability that the knife cuts between the two candles?**

# Solution

The solution can be found in `two-candles-one-cake.ipynb`.

A runnable version of the notebook exists at https://mybinder.org/v2/gh/sjtrny/two-candles-one-cake/HEAD?labpath=two-candles-one-cake.ipynb

# Generalisations

A prototype library is provided to calculate probabilities under different
probability distributions for each candle and the knife.

This example uses a Beta(2,2) distribution for the knife and uniform
distribution for both candles.

```
from utils import BetaBD, UniformBD, calculate_prob
from functools import partial

Beta22 = partial(BetaBD, a=2, b=2)

p = calculate_prob(Beta22, UniformBD, UniformBD)

print(p)
```

```
0.45
```

*WARNING*: I advise against using Piecewise defined functions for this as it
will likely cause sympy's integration system to fail.

## Problem History

I originally saw this problem presented by Ben Sparks on Numberphile https://www.youtube.com/watch?v=FkVe8qrT0LA.

This problems seems to have been around before hand though as I found it on New Scientist https://www.newscientist.com/article/mg24232361-100-puzzle-09-the-cake-and-the-candles/
