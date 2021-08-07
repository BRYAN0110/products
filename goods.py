import os
goods = []

#讀取檔案內項目
if os.path.isfile('goods.csv'):
	print('找到檔案拉~~~')
	with open('goods.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			goods.append([name, price])
else:
	print('找不到檔案拉.....')


#輸入商品名稱及價格
while True:
	name = input('請輸入物品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	goods.append([name, price])

print(goods)

#寫入到檔案
with open('goods.csv','w', encoding = 'utf-8') as f:
	for line in goods:
		f.write(line[0] + ',' + str(line[1]) + '\n')
