# with open("demo.txt" ,'r') as f:
#     data = f.read()
#     print(data)

with open("demo.txt", 'w') as f:
    data = f.write("Helo this in the with mode and we don't have to close the file in with mode since it automactically close the file")
    print(data)
