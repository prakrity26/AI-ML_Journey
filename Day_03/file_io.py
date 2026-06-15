# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print (type(data))
# f.close()



#  modes are read, write and append and another are:
#  r+ i.e read and overwrite - no truncate and pointer is on start 
#  w+ i.e read and overwrite - truncate 
#  a+ i.e read and append - no truncate and pointer is on end 

f = open("demo.txt",'w')
data = f.write("Hello I am using teh write mode ")
print(data)
f.close()