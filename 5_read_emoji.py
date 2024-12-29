# in this exercise we gonna learn how to read a story containing emojies 
# we have to gives the encoding detials like we had given 'encoding = utf-8'
# with open('love_story.txt', 'r' ,encoding='utf-8') as story:
#      print(story.encoding)
#      data = story.read()
#      print(data)



# if you have a very long data file and you want to read the specifics lines 
# we store read method in a variable 
# we use while loop here 

with open('long.txt', 'r') as f:
     data = f.read(100)
     while len(data) > 0:
          print(data)
          data = f.read(100)