# mehraj,100
# khan,50
# salman,200
# adnan,150
with open('exercise1.txt', 'r') as rf:
    with open('output1.txt','a') as wf:
        for i in rf.readlines():
            name,salary = i.split(',')
            wf.write(f'{name}, your salary is {salary}')


            