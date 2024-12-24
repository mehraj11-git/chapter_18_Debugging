# inthis exercise we will learn 
# how read the data of one csv file and write that data in other csv file
# suppose if you have a employees data like--name,address,salary etc..
# how will you separate the employers data as per there salary ,address ect..
# for reading ,we can use the dictreader and reader
# for writing,we can use the dictwriter and writer

from csv import DictReader,DictWriter
with open('final.csv','r') as rf:
    with open('output2.csv','w',newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['first_name','last_name','age'])
        csv_writer.writeheader()
        for line in csv_reader:
            fname,lname,age=line['firstname'],line['lastname'],line['age']
            csv_writer.writerow({
                'first_name':fname.upper(),
                'last_name':lname.upper(),
                'age':age
            })


# in this exercise first import the dictreader and dictwriter from csv
# open the file what we have to read
# and create a file for what we have to write in it by using 'w' mode 
# make objects and store them in variables separately
# in writer object give header names by using the 'fieldnames=' mode
# use the writerheader code then
# now, use the for loop to read the data of the exiting file 
# and store them in a varibale 
# followed by using the writerow 
# stuck in that!!!.........
# wait,first call parathesis and open dict inside it 
# key:value-----'first_name':fname
# now on the key write the fieldnames fro ex;first_name:
# and on value write the variable names that we made during for loop for ex:fname
# in this exercise we use upper method to write the names in caps