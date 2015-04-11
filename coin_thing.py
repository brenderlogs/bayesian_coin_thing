#Calculation of the Posterior Distribution of the Bias of a Coin from a Polynomial Prior.
#Brendan Cordy, 2014

import matplotlib.pyplot as plt
import numpy.linalg

#An object to represent the history of priors/posteriors before/after each flip.
class Dist_Sequence(object):
	
	def __init__(self,bins):
		self.bins = bins
		self.heads = 0
		self.tails = 0
		self.probs = [x/(float(bins)-1) for x in range(0,bins)]
		self.dist_list = []

	def add_prior(self,p_dist):
		self.dist_list = []
		self.dist_list.append(p_dist)
		return

	def add_heads_posterior(self,p_dist):
		self.dist_list.append(p_dist)
		self.heads+=1
		return

	def add_tails_posterior(self,p_dist):
		self.dist_list.append(p_dist)
		self.tails+=1
		return

	def get_probs(self):
		return self.probs

	def get_dist(self,n):
		return self.dist_list[n]

	def get_last_dist(self):
		return self.dist_list[len(self.dist_list)-1]

	def get_num_dists(self):
		return len(self.dist_list)

#Define a polynomial, to be used as a prior, from a list of points.
def define_prior(point_list,dist_seq):

	#Determine the unique polynomial of degree len(point_list) through the points in point_list.
	a = [[p[0]**n for n in range(0,len(point_list))] for p in point_list]
	b = [p[1] for p in point_list]
	poly_coeff = numpy.linalg.solve(a,b)

	#Initialize the distribution of p to the polynomial computed above.
	prior_poly = [sum([c*x**j for j,c in enumerate(poly_coeff)]) for x in probs]

	#Check the prior can be scaled to a density curve (never lies below the axis), and normalize it.
	neg = 0
	for x in prior_poly:
		if x < 0:
			neg = 1
	if neg == 1:
		p_dist = [1 for x in range(0,bins)]
		print "Invalid Prior: Interpolated distribution isn't non-negative."
	else:
		dist_seq.add_prior(normalize(prior_poly))
	return

#Normalize p_dist to a pmf while preserving proportions.
def normalize(p_dist):

	#Sum the probabilties and divide each entry by the result.
	totalweight = 0
	for r in range(0,bins):
		totalweight += p_dist[r]
	for r in range(0,bins):
		p_dist[r] = p_dist[r]/float(totalweight)

	#Plot the normalized prior.
	return p_dist

#Update after observing a head.
def flip_heads(dist_seq):

	prior = dist_seq.get_last_dist()
	p_dist = []

	#Calculate the total probability of flipping a head.
	prob_h = 0
	for i in range(0, bins):
		prob_h += (1 / float(bins)) * i * prior[i]

	#Update the probability of each value of p using Bayes' rule.
	for i in range(0, bins):
		p_dist.append(((1 / float(bins)) * i * prior[i]) / prob_h)

	dist_seq.add_heads_posterior(p_dist)
	return

#Update after observing a tail.
def flip_tails(dist_seq):

	prior = dist_seq.get_last_dist()
	p_dist = []

	#Calculate the total probability of flipping a tail.
	prob_t = 0
	for i in range(0, bins):
		prob_t += (1 / float(bins)) * (bins - i - 1) * prior[i]

	#Update the probability of each value of p using Bayes' rule.
	for i in range(0,bins):
		p_dist.append(((1 / float(bins)) * (bins - i - 1) * prior[i]) / prob_t)

	dist_seq.add_tails_posterior(p_dist)
	return

#Draw the current distribution of the probability of heads. 
def draw(dist_seq):

	#Draw prior and intermediates in shades of grey (pehaps fifty of them?)
	n = dist_seq.get_num_dists()-1
	for i in range(0,n):	
			plt.plot(dist_seq.get_probs(),dist_seq.get_dist(i),'-',color='grey',alpha=(i+1)/float(n+1))

	#Draw final posterior in red
	plt.plot(dist_seq.get_probs(),dist_seq.get_last_dist(),'-',color='red')

	frame = plt.gca()
	frame.set_title('Distribution of the Probability of Heads after ' + str(heads) + ' Heads and ' + str(tails) + ' Tails')
	frame.axes.get_yaxis().set_ticks([])
	plt.show()
	return

def main():
	dist_history = Dist_Sequence(1001)

	#Have the user define a prior.
	point_list = input('Enter a list of points in [0,1] x R+ to define a prior: ')
	define_prior(point_list, dist_history)

	#Have the user flip the coin.
	flip_result = raw_input('Flip the coin (H for heads, T for tails, D for done): ')
	#print flip_result

	while(flip_result != 'D'):
		if(flip_result == 'H'):
				flip_heads(dist_history)
		if(flip_result == 'T'):
				flip_tails(dist_history)
		flip_result = raw_input('Flip the coin (H for heads, T for tails, D for done): ')
	
	#Show the resulting sequence of distributions
	draw(dist_history)

if __name__ == '__main__':
    main()