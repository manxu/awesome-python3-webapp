def product(*x):
	c=1
	for k in x:
		c=c*k
	return c
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

def trim(s):
	if s[:1]!=' ' and s[-1:]!=' ':
		return s
	elif s[:1]==' ':
		return trim(s[1:])
	elif s[-1:]==' ':
		return trim(s[:-1])

def ite(**d):
	for k,v in d.items():
		print(k,v)


def findMinAndMax(L):
	max=L[0]
	min=L[0]
	for x in L:
		if x>max:
			max =x
		if x<min:
			min=x
	return (min,max)
def trig():
	L=[1]
	while True:
		yield L
		L.insert(0,0)
		L.append(0)
		L=[L[i]+L[i+1] for i in range(len(L)-1)]

def _up():
	cp=0
	def u():
		nonlocal cp
		cp=cp+1
		return cp
	return u
if __name__=='__main__':
	try:
		print('try...')
		r=10/1
	except ZeroDivisionError as e:
		print('except:',e)
	else:
		print('else')
	finally:
		print('finally...')
	print('END')