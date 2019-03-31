import os
def update_attend():
	print('root:',os.getcwd())
	with open('./attend/test1.txt', 'r') as f :
		lines = f.readlines()
		attend = {} #sorting 하기
		for i in lines:
			a = i.strip()
			a = a.split(' ')
			attend[a[0]] = a[1]
		f.close()
	attend = dict(sorted(attend.items()))
	return attend