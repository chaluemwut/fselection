import sys
from method_selection import *

def load_data():
	x = loadtxt('fselect.txt', delimiter=',', dtype=int)
	y = loadtxt('fresult.txt', dtype=int)
	return x,y

try :
	arg = sys.argv[1]
except Exception, e:
	arg = ''

print 'start'
x,y = load_data()
if arg == 'chi2':
	method = Chi2(x, y)
elif arg == 'bf':
	method = BruteForce(x, y)
else:
	method = Chi2(x, y)

method.process()
print 'end'