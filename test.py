test = []
with open('test.csv','r',encoding = 'utf-8') as f:
	for line in f:

		t = line.strip().split(',')
		print(t)

		# if '學生,成績' in line:
		#	continue
		# name, grade = line.strip().split(',')
		# test.append([name, grade]) 


while True:
	name = input('請輸入姓名:')
	if name == 'q':
		break
	grade = input('請輸入成績:')
	test.append([name, grade])
with open('test.csv', 'w', encoding = 'utf-8') as f:
	f.write('姓名,成績\n')
	for g in test:
		f.write(g[0] + ',' + str(g[1]) + '\n')
