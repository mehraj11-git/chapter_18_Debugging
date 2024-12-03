# what is debugging ?
# Debugging is the process of finding and resolving defects or problems
# within a computer program that prevent correct operation of computer software or a system 
# what is module ??
# modules are the python file contains the useful classes and functions 

# steps for debugging 
# 1.) set trace
# 2.) execute code link by line
import pdb
pdb.set_trace()
name = input('enter your name : ')
age = input('enter your age : ')
print(f'Hello {name} your age is {age} ')
age2 = int(age) + 5
print(f'{name} you will be {age2} in the next five years ')


# there is a problem or defect is in this code                      # l --list
# to find it we have to import the PBD                              # c -- continue
# and call the set trace func                                       # n -- next
# in terminal it shows the defect location                          # q --quit
# we use the l command to see the list
# and we want to move further even the code has error we use the n commond
# we check the variable exit or not 
# for ex here i check the name variable 
# to quit the pdb we use the q commond 
# we use c command to stop the execution and to continue the code 
# we can write the set trace where we want to write 