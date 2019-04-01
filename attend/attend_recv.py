import os
def update_attend():
	PATH = ""
	if os.getcwd() == '/home/ubuntu/workspace/pocheck':
		PATH = './attend'
	else :
		PATH = '/home/bicsu/PoCheck/attend'		
	with open(PATH+'/test1.txt', 'r') as f :
		lines = f.readlines()
		attend = {} #sorting 하기
		for i in lines:
			a = i.strip()
			a = a.split(' ')
			attend[a[0]] = a[1:]
		f.close()
	for i in attend :
		if attend[i][1] != '0':
			attend[i][1] = attend[i][1][11:]	
	attend = dict(sorted(attend.items()))
	return attend
	



