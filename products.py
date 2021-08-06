products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []
	p.append(name)
	p.append(price)
	# so called p = [name, price]
	products.append(p)
	# so called products.append([name, price]) 
for p in products:
	print(p[0],'的價格為:',p[1])