# 'w'    'a'   'r+'
# with open('file3.txt' , 'w') as w:
#     w.write('hello')


# with open('file4.txt' , 'a') as w:
#     w.write('\nadd this line\nadd this one as well')

# import pdb
# pdb.set_trace()

# with open('file4.txt','r+') as f:
#     f.seek(len(f.read()))
#     f.write('\nwhy i cant add this ')

with open('file.txt','r') as rf:
    with open('file4.txt','w') as wf:
        wf.write(rf.read())




# 'W' mode create the file and write in it 
# this mode delete the data and add the new one 
# hence,use this mode in a empty file 

# 'a' ----> append 
# 'a' mode donot delete the existing data ,perhaps add the new data 
# this method also create a new file 


# 'r+' mode use for both read and write 
# this mode 'donot' create the file
# we use seek mode to write after the sentence 

# echo -e---->command
# we create the files the with this command

# suppose if u wanna read the file and add this file on another file 