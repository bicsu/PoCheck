import os
def update_attend():
	PATH = ""
	if os.getcwd() == '/home/bicsu/PoCheck/attend':
		PATH = '/home/bicsu/PoCheck/attend'
	elif os.getcwd() == '/home/ubuntu/workspace/pocheck':
		PATH = './attend'		
	with open(PATH+'/test1.txt', 'r') as f :
		lines = f.readlines()
		attend = {} #sorting 하기
		for i in lines:
			a = i.strip()
			a = a.split(' ')
			attend[a[0]] = a[1]
		f.close()
	attend = dict(sorted(attend.items()))
	return attend
print(os.getcwd())