# # How to open a file

# # open("the path of the file",'mode')
# #Modes 'r','w, 'a','b'

# #READING FROM A FILE
# # def file_handling():
# #     file=open('data.txt','r')    
# #     return file.read()
# # print(file_handling())

# file2=open("data.txt", 'r')
# lines = file2.readlines()
# while lines:
#     print(lines, end=" ") # end=" " to avoid double readlines
#     lines=file2.readline()
# file2.close()

# file=open("data.txt", 'r')
# lines=file.readlines()
# for line in lines:
#     print(line, end=' ')
# file.close()


#WRITE TO A FILE
#write()
file=open('data.txt','w')
file.write(" But Javascript is the thing.\n")
file.close()


#WITH

    
with open('data.txt', 'a') as file:
    file.write("This is sentence three\n")
    file.write("This is sentence four\n")
    
with open('data.txt', 'r') as file:
    content=file.read()
    print(content)   

    