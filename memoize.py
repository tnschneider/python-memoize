import time, collections, json

def memoize(func):
	cache = {}
	def wrapped(*args, **kwargs):
		hashable = True
		for arg in args:
			if not isinstance(arg, collections.Hashable):
				hashable = False
				break
		if hashable:
			key = json.dumps({ "args": args, "kwargs": kwargs })
			if key in cache:
				return cache[key]
		res = func(*args, **kwargs)
		if hashable: cache[key] = res
		return res
		
	return wrapped

def timed(func):
	def wrap(*args, **kwargs):
		st = time.time()
		res = func(*args, **kwargs)
		end = time.time()
		return { 'result': res, 'time': end - st }

	return wrap

@timed
@memoize
def echo(n):
	for i in range(10000000):
		n += i
	return n

print(echo(100))
print(echo(100))
print(echo(100))