import sys, getopt
from method_selection import *

def load_data():
	x = loadtxt('fselect.txt', delimiter=',', dtype=int)
	y = loadtxt('fresult.txt', dtype=int)
	return x,y

myopts, args = getopt.getopt(sys.argv[1:],"m:k:t")
m_arg = ''
k_arg = 0
simple_plot = ''
for o, a in myopts:
    if o == '-m':
        m_arg=a
    elif o == '-k':
        k_arg=int(a)
    elif o == '-t':
    	simple_plot='sp'
    else:
        print("Usage: %s -i input -o output" % sys.argv[0])

print 'start'
x,y = load_data()
if simple_plot == 'sp':
	tool = ToolUtil()
	tool.simple_plot(x, 20)
	quit()

if m_arg == 'chi2':
	method = Chi2(x, y)
elif m_arg == 'bf':
	method = BruteForce(x, y)
else:
	method = Chi2(x, y)

if k_arg != 0:
	method.process(k_num=k_arg)
else:
	method.process()
print 'end'