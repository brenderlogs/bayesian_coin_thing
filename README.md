# bayesian_coin_thing
Visualization of Bayesian updating.

- Provide a list of n points, which define a prior distribution of the probability of heads for a coin of unknown bias. The unique polynomial of degree n-1 through these points is calculated, checked for non-negativity on [0,1], and then scaled to obtain a probability distribution. Try [(0,0),(0.5,1),(1,0)].

- Input the results of several coin flips with H and T. When you're done flipping, enter D to calculate and draw the updated distribution after every flip. The resulting posterior distribution, after observing the entire sequence of flips, is shown in red, and the prior is shown in dashed black. The intermediates are shown in grey, with increasing alpha as more evidence is considered.

<p align="center">
<img src="https://github.com/brenderlogs/bayesian_coin_thing/blob/master/draw_demo.png?raw=true"/>
</p>

##

Requires matplotlib and numpy. If you're new to python, just use a distribution like [Anaconda](http://continuum.io/downloads) that comes with these packages installed. Fire it up and type `execfile('/path/to/coin_thing.py')`.
