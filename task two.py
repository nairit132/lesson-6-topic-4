s1 = {2,3,1,}
s2 = {'a','b','c'}
s3 = list(zip(s1 , s2))
print(s3,"\n")
list1 = [10,20,30,40]
list2 = [100,200,300,400]
for x , y in zip(list1 , list2):
    print(x,y)
stocks = ['GOOG', 'AAPL', 'MSFT', 'AMZN']
prices = [891.1, 416.35, 64.09, 1530.25]
new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))
