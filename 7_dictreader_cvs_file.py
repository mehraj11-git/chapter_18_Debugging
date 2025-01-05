# we will read the csv file with dictreader 
# we have to follow the same steps as we did in reader func 
# here we can print seprate values like name email ect...
# this is more better than reader func
# now the tricky is here !!!
# think,what if there is no comma instead there is another delimeter
# puase!!!error!!! for that we have to tell the python that what kind of  delimeter we have ....
from csv import DictReader

with open('csv1.csv','r') as f:
    # csv_reader = DictReader(f) 
    csv_reader = DictReader(f,delimiter='|')
    for i in csv_reader:      #1
        print(i['name'])
        print(i['email'])
        print(i['phone'])