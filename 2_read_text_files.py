# readfile 
# open function
#  read method
# seek method
# tell method
# readline method
# readlines method
# close method

# to read the file we use the open func to take the path first
# we use the r mode to read it
# if we donot write any mode ,by defult it will take read mode
# we use close mode after reading the file
# we cant print more than one time ,bcz it will read as cursor 
# we use tell method to check where is our cursor position
# we use seek method to change the cursor position
# for print just one line we use readline mode 
# here the files are located in same folder 
# if the folders are located in diff  folders we have to use the path
# we use readlines to read specific line by using slicing method 


# f = open('files.txt,' 'r') 
# to know the name of the file we use 
# name and closed 

f1 = open(r'c:\python tutorial\chapter_16_OOP.py/file2.txt')
# f = open('file1.txt')     

# print(f'cursor position - {f.tell()}') 
# print(f.read())
# print(f'cursor position - {f.tell()}')
# print('before seek method')
# f.seek(0)
# print('after seek method')
# print(f'cursor position - {f.tell()}')


print(f1.read())
# # print(f.readline()) 
# # print(f.readline()[:2]) 
# lines = f.readlines()
# # print(len(lines))
# for line in lines:
#     print(line,end = '')

# print(f.name)
# print(f.closed)
# f.close()
# print(f.closed)

# we can read the file with "with block " method 
# we call this method contast manager
with open('file1.txt') as f:
    data = f.read()
    print(data)

print(f.closed)   #1

# first we have to write the with and the file name followed by anyword(object)
# and then store it in a variable and print it
# its a lengthy code ...isn't?? 
# it is,but with this method we donot need to close the file 
# it will automatically close it 
# to check we print it  1