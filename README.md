# bayesian_coin_thing
Visualization of Bayesian updating.

- Provide a list of n points, which define a prior distribution of the probability of heads for a coin of unknown bias. The unique polynomial of degree n-1 through these points is calculated, checked for non-negativity on [0,1], and then scaled to obtain a probability distribution. Try [(0,0),(0.5,1),(1,0)].

- Input the results of several coin flips with H and T. When you're done flipping, enter D to draw the sequence of updated posteriors. The resulting distribution is shown in red, and the intermediates are shown in grey. The original prior has the lowest alpha.

![Demo Run](draw_demo.png)

## setup

Requires matplotlib and numpy. I run it using [Anaconda](http://continuum.io/downloads) on Windows, which comes with these packages installed. Just open the Python interpreter and type `execfile('C:/path/to/coin_thing.py')`.
