from numpy import *
from sklearn.decomposition import PCA
import pylab as pl

color_list = ['red','red', 'green', 'yellow', 'black', 'blue', 'orange', 'pink', 'gray', 'brown', 'violet']
def load_data():
	x = loadtxt('fselect.txt', delimiter=',', dtype=int)
	y = loadtxt('fresult.txt', dtype=int)
	return x,y

def plot_all(x, y):
	pca = PCA(n_components=2)
	new_x = pca.fit(x).transform(x)
	for i in range(0, len(new_x)):
		l_color = color_list[y[i]]
		pl.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
	pl.show()

def plot_2(x, y):
	pca = PCA(n_components=2)
	new_x = pca.fit(x).transform(x)
	for i in range(0, len(new_x)):
		cred_class = y[i]
		l_color = ''
		if cred_class >= 5:
			l_color = 'red'
		else:
			l_color = 'green'
		# l_color = color_list[y[i]]
		pl.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
	pl.show()	

def plot_10(x, y):
	fig = pl.figure()
	pca = PCA(n_components=2)
	new_x = pca.fit(x).transform(x)
	for i in range(0, len(new_x)):
		cred_class = y[i]
		l_color = color_list[cred_class]
		ax1 = fig.add_subplot(911)
		ax2 = fig.add_subplot(912)
		ax3 = fig.add_subplot(913)
		ax4 = fig.add_subplot(914)
		ax5 = fig.add_subplot(915)
		ax6 = fig.add_subplot(916)
		ax7 = fig.add_subplot(917)
		ax8 = fig.add_subplot(918)
		ax9 = fig.add_subplot(919)				
		# ax10 = fig.add_subplot(1021)
		if cred_class == 1:
			ax1.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
		elif cred_class == 2:
			ax2.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
		elif cred_class == 3:
			ax3.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
		elif cred_class == 4:
			ax4.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
		elif cred_class == 5:
			ax5.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
		elif cred_class == 6:
			ax6.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
		elif cred_class == 7:
			ax7.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
		elif cred_class == 8:
			ax8.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
		elif cred_class == 9:
			ax9.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
		# elif cred_class == 10:
		# 	ax10.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
		# pl.scatter(new_x[i, 0], new_x[i, 1], color=l_color)
	pl.show()

x, y = load_data()
plot_2(x, y)
# fig = pl.figure()
# ax1 = fig.add_subplot(211)
# ax1.plot([(1, 2), (3, 4)], [(4, 3), (2, 3)])
# ax2 = fig.add_subplot(212)
# ax2.plot([(7, 2), (5, 3)], [(1, 6), (9, 5)])
# pl.show()
