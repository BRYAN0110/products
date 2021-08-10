#寫入資料
def find_file(filename):
    products= []
    with open(filename, 'r', encoding = "utf-8") as f:
        for line in f:
            if '商品, 價格' in line:
                continue
            else:
                name, price= line.strip().split(',')
                products.append([name, price])
    return(products)

#輸入資料
def file_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('請輸入商品價格:')
        products.append([name, price])
    return(products)

#顯示出資料內容
def print_file(products):
    for p in products:
        print(p[0], '的價格為:', p[1], '\n')

#將資料寫入檔案
def write_file(products, filename):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for line in products:
            f.write(line[0]+ ','+ line[1]+ '\n')


import os

if os.path.isfile('products.csv'):
    print('找到檔案了!')
    products= find_file('products.csv')
else:
    print('找不到檔案!')
    products= []
products= file_input(products)
print_file(products)
write_file(products, 'products.csv')