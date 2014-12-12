from numpy import *
from sklearn.feature_selection import *
import pylab as pl

def load_data():
	x = loadtxt('fselect.txt', delimiter=',', dtype=int)
	y = loadtxt('fresult.txt', dtype=int)
	return x,y

print 'start process'
x,y = load_data()
x_new = SelectKBest(chi2, k=4).fit_transform(x,y)

# count = 0
# for x_select in x:
# 	for x_new_select in x_new:
# 		if array_equal(x_select, x_new_select) :
# 			print 'counter data ', count
# 	count+=1
np_x = array(x)
np_x = np_x.transpose()
np_x_new = array(x_new)
np_x_new = np_x_new.transpose()

# print 'x old'
# print np_x
# print 'x new'
# print np_x_new
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
# print i_select
# print 'x old'
# np_x = array(x)
# print len(np_x.transpose())
# print 'x new'
# np_x_new = array(x_new)
# print np_x_new.transpose()

for i in range(1,2000):
	pl.plot(x[i])
pl.xlabel('Feature')
pl.ylabel('Occures')
base_x = 0.80
base_y = 0.76
pl.figtext(base_y, base_x-0.05*(-1), '** Red is chi-2 select feature **')
if 0 in i_select:
	pl.figtext(base_y, base_x-0.05*0, '0 - location', color='red')
else:
	pl.figtext(base_y, base_x-0.05*0, '0 - location')
if 1 in i_select:
	pl.figtext(base_y, base_x-0.05*1, '1 - shares', color='red')
else:
	pl.figtext(base_y, base_x-0.05*1, '1 - shares')
if 2 in i_select:
	pl.figtext(base_y, base_x-0.05*2, '2 - comments', color='red')
else:
	pl.figtext(base_y, base_x-0.05*2, '2 - comments')
if 3 in i_select:
	pl.figtext(base_y, base_x-0.05*3, '3 - like', color='red')
else:
	pl.figtext(base_y, base_x-0.05*3, '3 - like')
if 4 in i_select:
	pl.figtext(base_y, base_x-0.05*4, '4 - vdo', color='red')
else:
	pl.figtext(base_y, base_x-0.05*4, '4 - vdo')
if 5 in i_select:
	pl.figtext(base_y, base_x-0.05*5, '5 - images', color='red')
else:
	pl.figtext(base_y, base_x-0.05*5, '5 - images')
if 6 in i_select:
	pl.figtext(base_y, base_x-0.05*6, '6 - url', color='red')
else:
	pl.figtext(base_y, base_x-0.05*6, '6 - url')
if 7 in i_select:
	pl.figtext(base_y, base_x-0.05*7, '7 - tags', color='red')
else:
	pl.figtext(base_y, base_x-0.05*7, '7 - tags')
pl.show()
print 'end process'