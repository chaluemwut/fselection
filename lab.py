def f():
	for i in range(8, 0):
		yield i

g = f()
for i in g:
	print i.next()
