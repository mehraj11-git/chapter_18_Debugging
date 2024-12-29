# CSV file ---> comma seprated value 
# this file use to store data as like we add in txt file 
# but in this CVS file we store tables,box ect...
# to read CSV file we use the module 
# that module has the reader func

from csv import reader

with open('csv1.csv','r') as f:
    csv_reader = reader(f)
    # print(csv_reader)
    next(csv_reader)
    for i in csv_reader:      #1
        print(i)




# import the func from module and 
# open the file with mode(read,write,etc..) 
# and make a variable contianing the file with reader func
# this is iterator
# we can do looping here
# we cant do more than one loop here ,to do so we have to store this 1 in list 
# if we print this will print the heqading as well 
# as we donot need the heading ,hence we use the next method
# we can extract particular items ,value ect by using the if else method


