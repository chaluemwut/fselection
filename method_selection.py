from numpy import *
import pylab as pl
from sklearn.feature_selection import *


class BaseMethod(object):

	def get_select(self, np_x, np_x_new):
		i_select = []
		for x_t in np_x_new:
		 	if array_equal(x_t, np_x[0]):
		 		i_select.append(0)
		 	elif array_equal(x_t, np_x[1]):
		 		i_select.append(1)
		 	elif array_equal(x_t, np_x[2]):
		 		i_select.append(2)
		 	elif array_equal(x_t, np_x[3]):
		 		i_select.append(3)
		 	elif array_equal(x_t, np_x[4]):
		 		i_select.append(4)
		 	elif array_equal(x_t, np_x[5]):
		 		i_select.append(5)
		 	elif array_equal(x_t, np_x[6]):
		 		i_select.append(6)
		 	elif array_equal(x_t, np_x[7]):
		 		i_select.append(7)
		return i_select

	def transpose_array(self, x, x_new):
		np_x = array(x)
		np_x = np_x.transpose()
		np_x_new = array(x_new)
		np_x_new = np_x_new.transpose()
		return np_x, np_x_new

class BruteForce(BaseMethod):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def process(self):
		print 'start brute'

class Chi2(BaseMethod):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def process(self):
		print 'start chi2'
		x_new = SelectKBest(chi2, k=4).fit_transform(self.x ,self.y)
		np_x, np_x_new = self.transpose_array(self.x, x_new)
		i_select = self.get_select(np_x, np_x_new)

		for i in range(1, 2000):
		 	pl.plot(self.x[i])
		
		pl.xlabel('Feature')
		pl.ylabel('Occures')
		base_x = 0.80
		base_y = 0.76
		pl.figtext(base_y, base_x-0.05*(-1), '** Orange is chi-2 select feature **')
		color_graph = 'orange'
		if 0 in i_select:
			pl.figtext(base_y, base_x-0.05*0, '0 - location', color=color_graph)
		else:
			pl.figtext(base_y, base_x-0.05*0, '0 - location')
		if 1 in i_select:
			pl.figtext(base_y, base_x-0.05*1, '1 - shares', color=color_graph)
		else:
			pl.figtext(base_y, base_x-0.05*1, '1 - shares')
		if 2 in i_select:
			pl.figtext(base_y, base_x-0.05*2, '2 - comments', color=color_graph)
		else:
			pl.figtext(base_y, base_x-0.05*2, '2 - comments')
		if 3 in i_select:
			pl.figtext(base_y, base_x-0.05*3, '3 - like', color=color_graph)
		else:
			pl.figtext(base_y, base_x-0.05*3, '3 - like')
		if 4 in i_select:
			pl.figtext(base_y, base_x-0.05*4, '4 - vdo', color=color_graph)
		else:
			pl.figtext(base_y, base_x-0.05*4, '4 - vdo')
		if 5 in i_select:
			pl.figtext(base_y, base_x-0.05*5, '5 - images', color=color_graph)
		else:
			pl.figtext(base_y, base_x-0.05*5, '5 - images')
		if 6 in i_select:
			pl.figtext(base_y, base_x-0.05*6, '6 - url', color=color_graph)
		else:
			pl.figtext(base_y, base_x-0.05*6, '6 - url')
		if 7 in i_select:
			pl.figtext(base_y, base_x-0.05*7, '7 - tags', color=color_graph)
		else:
			pl.figtext(base_y, base_x-0.05*7, '7 - tags')
		pl.show()

