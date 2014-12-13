from numpy import *
import pylab as pl
from sklearn.feature_selection import *
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
from sklearn import svm

default_k = 4

class ToolUtil(object):
	def __init__(self):
		pass

	def simple_plot(self, x, k):

		lst = []
		counter = 0;
		for i in range(0, len(x)):
			b = 0 in x[i]
			less100 = [xi for xi in x[i] if xi > 10]
			if b != False and len(less100) == 0:
				counter+=1
				if counter > k:
					break
				lst.append(x[i])
		for j in range(0, len(lst)):
			pl.plot(lst[j])
		base_x = 0.80
		base_y = 0.76			
		pl.figtext(base_y, base_x-0.05*0, '0 - location')
		pl.figtext(base_y, base_x-0.05*1, '1 - shares')
		pl.figtext(base_y, base_x-0.05*2, '2 - comments')
		pl.figtext(base_y, base_x-0.05*3, '3 - like')
		pl.figtext(base_y, base_x-0.05*4, '4 - vdo')
		pl.figtext(base_y, base_x-0.05*5, '5 - images')
		pl.figtext(base_y, base_x-0.05*6, '6 - url')
		pl.figtext(base_y, base_x-0.05*7, '7 - tags')
		pl.show()


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

	def process(self, k_num=default_k):
		print 'start brute'
		cv_errors = []
		kfold = KFold(len(self.x), n_folds=10)
		nfeatures = range(0, 8)
		x_tran = transpose(self.x)
		x_r=[]
		for nfeature in nfeatures:
			rmses = []
			x_r.append(x_tran[nfeature])
			x_select = transpose(x_r)
			for train, test in kfold:
				xtrain, ytrain, xtest, ytest = x_select[train], self.y[train], x_select[test], self.y[test]
				clf = svm.SVC()
				clf.fit(xtrain, ytrain)
				ypred = clf.predict(xtest)
				rmses.append(sqrt(mean_squared_error(ypred, ytest)))
			cv_errors.append(mean(rmses))
		fig = pl.figure()
		ax = fig.add_subplot(111)
		pl.plot(nfeatures, cv_errors)
		for xy in zip(nfeatures,cv_errors):
			ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='offset points')
		pl.title('Brute force')
		pl.show()




class Chi2(BaseMethod):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def process(self, k_num=4):
		print 'start chi2'
		x_new = SelectKBest(chi2, k=k_num).fit_transform(self.x ,self.y)
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

