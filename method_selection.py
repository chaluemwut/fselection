from numpy import *
import pylab as pl
from sklearn.feature_selection import *
from sklearn.cross_validation import *
from sklearn.metrics import mean_squared_error
from sklearn import svm
import itertools

default_k = 4
all_feature = array(['location', 'shares', 'comments', 'like', 'vdo', 'images', 'url', 'tags'])

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
	
	def add_label(self, feature_result, min_feature_label):
		base_x = 0.88
		base_y = 0.74
		for i in range(0, len(feature_result)):
			x1 = feature_result[i]
			x2 = min_feature_label[i]
			pl.figtext(base_y, base_x-0.05*i, '{} -> [{}]'.format(x1, x2))
	
	def feature_label(self, data):
		f = data[0]
		s = data[1]
		base_x = 0.88
		base_y = 0.74
		for i in range(0, len(data[0])):
			 pl.figtext(base_y, base_x-0.05*i, '{} -> {}'.format(f[i], s[i]))
	
	def feature_label_all(self):
		f = list(range(1, 9))
		self.feature_label((f,all_feature))		

class OrginModel(BaseMethod):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def process(self):
		x_ax = list(range(1, 9))
		pl.title('Origin Model')
		self.feature_label_all()
		for data in self.x:
			pl.plot(x_ax, data)
		pl.show()
	
class BruteForce(BaseMethod):
	feature_lst = '01234567'


	def __init__(self, x=None, y=None):
		self.x = x
		self.y = y

	def compute_selection(self, range_method):
		rmses = {}
		for i in range_method:
			print i
			lst = list(itertools.combinations(self.feature_lst, i))
			rmses_i = []
			rmses_feature = []
			for f_select in lst:
				x_tran = transpose(self.x)
				i_feature = [int(x) for x in list(f_select)]
				x_feature = transpose(x_tran[i_feature])
				x_train, x_test, y_train, y_test = train_test_split(x_feature, self.y, test_size=0.3, random_state=0)				
				clf = svm.SVC()
				clf.fit(x_train, y_train)
				ypred = clf.predict(x_test)
				rmses_i.append(sqrt(mean_squared_error(ypred, y_test)))
				rmses_feature.append(f_select)				
			rmses_min = min(rmses_i)
			r_index = rmses_i.index(rmses_min)
			rmses[rmses_feature[r_index]] = rmses_i[r_index]
		return rmses
	
	def plot_rmse(self, rmses, title_msg):
		min_result = [None]*8
		min_feature_label = [None]*8
		for key in rmses.keys():
			min_result[len(key)-1] = round(rmses[key], 3)
			min_feature_label[len(key)-1] = ','.join(key)
		fig = pl.figure()
		ax = fig.add_subplot(111)
		feature_result = list(range(1, 9))
		for xy in zip(feature_result, min_result):
			ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='offset points')
		pl.title(title_msg)
		self.add_label(feature_result, min_feature_label)
		pl.plot(feature_result, min_result)
		pl.show()		
			
	def forward(self):
		print 'Forward'
		rmses = self.compute_selection(range(1,9))
		self.plot_rmse(rmses, 'Feature selection : Forward')

	def backward(self):
		print 'Back ward'
		rmses = self.compute_selection(range(8, 0, -1))
		self.plot_rmse(rmses, 'Feature selection : Backward')

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

	def create_new_model(self, mtype):
		range_method = ''
		if mtype == 'forward':
			range_method = range(1, 9)
		else:
			range_method = range(8, 0, -1)

# 		rmse = {('2', '3'): 2.998908694034462, ('1', '2', '3', '6'): 2.9824911873277555, ('0', '1', '2', '3', '4', '6', '7'): 3.1242675082609561, ('2', '3', '7'): 2.972872439257729, ('2', '3', '4', '6', '7'): 3.0894996655293645, ('2',): 3.564004441576142, ('1', '2', '3', '4', '6', '7'): 3.0818087234906884, ('0', '1', '2', '3', '4', '5', '6', '7'): 3.2440301459082304}
		rmse = self.compute_selection(range_method)
		v_rmse = rmse.values()
		key_rmse = rmse.keys()
		min_rmse = min(v_rmse)
		index_min = v_rmse.index(min_rmse)
		feature = key_rmse[index_min]
		feature_list = [int(x) for x in list(feature)]
		
		feature_tran = transpose(self.x)
		f_temp = feature_tran[feature_list]
		f_select = transpose(f_temp).tolist()
		x_ax = list(range(1, len(feature_list)+1))
		
		f_label = list(range(1, len(feature_list)+1))
		s_label = all_feature[feature_list]
		self.feature_label((f_label, s_label))
		for p in f_select:
			pl.plot(x_ax, p)
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

	def create_new_model(self, k_num=4):
		x_new = SelectKBest(chi2, k=k_num).fit_transform(self.x ,self.y)
		print 'x new ', x_new
		np_x, np_x_new = self.transpose_array(self.x, x_new)
		i_select = self.get_select(np_x, np_x_new)
		
# 		print np_x_new
		
		f_label = list(range(1, len(i_select)+1))
		s_label = all_feature[i_select]
		self.feature_label((f_label, s_label))
		
		for i in x_new:
		 	pl.plot(f_label, i)
		pl.show()
		

def load_data():
	x = loadtxt('vmodel.txt', delimiter=',', dtype=int)
	y = loadtxt('fresult.txt', dtype=int)
	return x,y

# x,y = load_data()
# bf = BruteForce(x, y)
# bf.backward()