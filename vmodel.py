import sys, getopt
from method_selection import *

def load_data():
	x = loadtxt('fselect.txt', delimiter=',', dtype=int)
	y = loadtxt('fresult.txt', dtype=int)
	return x,y

myopts, args = getopt.getopt(sys.argv[1:],"m:k:t:e:c:")
m_arg = ''
k_arg = 0
simple_plot = ''
rmse = ''
create = ''
for o, a in myopts:
    if o == '-m':
    	print a
        m_arg=a
    elif o == '-k':
        k_arg=int(a)
    elif o == '-t':
    	simple_plot='sp'
    elif o == '-e':
    	rmse=a
    elif o == '-c':
    	create=a
    else:
        print("Usage: %s -i input -o output" % sys.argv[0])

print 'start'
x,y = load_data()
if simple_plot == 'sp':
	tool = ToolUtil()
	tool.simple_plot(x, 20)
	quit()

if rmse == 'forward':
	method = BruteForce(x,y)
	method.forward()
	exit()
elif rmse == 'backward':
	method = BruteForce(x,y)
	method.backward()
	exit()

if m_arg == 'chi2':
	method = Chi2(x, y)
elif m_arg == 'bf':
	method = BruteForce(x, y)
elif m_arg == 'origin':
	method = OrginModel(x, y)
	method.process()
	exit()

if create == 'forward':
	method.create_new_model('forward')
	exit()
elif create == 'backward':
	method.create_new_model('backward')
	exit()
elif create == 'chi2':
	if k_arg != 0:
		method.create_new_model(k_arg)
	else:
		method.create_new_model()
	exit()

if k_arg != 0:
	method.process(k_num=k_arg)
else:
	method.process()

print 'end'