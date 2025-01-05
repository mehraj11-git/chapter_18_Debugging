# there are two ways to write in csv file 
# first writer and second dictwriter
# import the writer from csv
# and then use with open and create a new file by giving the name followed by 'w' or 'a' 
# store the object in variable 
# now,again we have to two func to print it 
# writerow ---> in this method u have to create one list only
# writerows--->create list inside list containing all data
from csv import writer
with open('writing.csv','w',newline= '') as w:   #1
    csv_writer = writer(w)
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['khaled','INDIA'])
    # csv_writer.writerow(['mehraj','CANADA'])
    csv_writer.writerows([['name','country'],['yousuf','portugul'],['mehraj','CANADA']])
# here we get the data with blank line 
# to remove this blank lines we use the newline = '' at 1