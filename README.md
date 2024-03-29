# Two Candles, One Cake

# Problem

Suppose that you have a [Battenburg cake](https://en.wikipedia.org/wiki/Battenberg_cake), which is 1 unit long.

You then:
- place two candles at random positions along the length
- randomly cut the cake across the length

*What is the probability that the knife cuts between the two candles?*

<img src="https://github.com/sjtrny/two-candles-one-cake/raw/main/battenburg.jpg" width="400">

# Solution

When the candles and knife are uniformly distributed the probability that the knife is between both candles is 

$$P(C_{1,2} < K < C_{1,2}) = \frac{1}{3}$$

# Working and Code

Full working is provided in [the main notebook](https://github.com/sjtrny/two-candles-one-cake/blob/main/two-candles-one-cake.ipynb).

A live version of the notebook can be launched on [mybinder.org](https://mybinder.org/v2/gh/sjtrny/two-candles-one-cake/HEAD?labpath=two-candles-one-cake.ipynb).

# In Progress (Currently broken): Generalisations 

A prototype library is provided to calculate probabilities under different
probability distributions.

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
