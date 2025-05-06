# Two Candles, One Cake

Interactive visualisations here https://visual-candles-cake.sjtrny.com

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

# Alternative Solution

An alternative solution using two dependent variables is presented in the [dependent-alternative](https://github.com/sjtrny/two-candles-one-cake/blob/main/dependent-alternative.ipynb) notebook.

