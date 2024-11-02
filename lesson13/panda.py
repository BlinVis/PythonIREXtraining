import csv

import pandas as pd
products=['apples','grapes','oranges','bananas']
sales=[150,200,180,90]
sales_series= pd.Series(sales,index=products)
print(sales_series)
print(sales_series['grapes'])


#
best_selling_product= sales_series.idxmax()
print(f'Best selling product is : {best_selling_product}')




















#data={'Name':['arizon','John','Michael'],
      #'Age':[21,59,32],
      #'City':['prishtine','nyc','London']
    # }

#df=pd.DataFrame(data)
#print(df)


data=[
    ['Name','Age','City'],
    ['a',13,'pr'],
    ['b',18,'nyc'],
    ['c',13,'usa'],





    ]
with open('example.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data)

    print('data written to example.csv')

with open ('example.csv','r') as file :
    reader=csv.reader(file)
    for row in reader:
        print(row)


