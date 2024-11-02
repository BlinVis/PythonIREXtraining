
import csv

data=[
    {'name': 'Arion','Age': 21, 'city':'Prishtine'},
    {'name': 'Fat', 'Age': 17, 'city': 'Prishtine'},
    {'name': 'Klea', 'Age': 17, 'city': 'Prishtine'},




]

header= ['name','Age','city']

with open('people.csv','w', newline='') as file:
    writer=csv.DictWriter(file,fieldnames=header)

    writer.writeheader()
    writer.writerows(data)
print('data written to people.csv')

with open('people.csv','r') as file:
    reader= csv.DictReader(file)
    for row in reader:
        print(dict(row))

