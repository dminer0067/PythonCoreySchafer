# f = open("PythonWiki.txt","r")

# with open("PythonWiki.txt","r") as f:
#     for line in f:
#         print(line,end='')
    
    # f_content = f.readline()
    # print(f_content,end="")
    
    # f_content = f.readline()
    # print(f_content,end="")
   
# print(f.name)
# print(f.mode)
# #print(f.closed)

# print(f.read())



# with open("PythonWiki.txt","r") as f:
#     size_to_read = 10
#     f_cont = f.read(size_to_read)
#     print(f_cont,end="")
    
#     f.seek(0)
    
#     f_cont = f.read(size_to_read)
#     print(f_cont)
    
    #print(f.tell())
    # while len(f_cont) > 0:
    #     print(f_cont,end='*')
    #     f_cont = f.read(size_to_read)
        
#write into file
# with open("test1.txt","w") as f:
#     f.write("test data")
#     f.seek(0)
#     f.write("R")


# with open("File1.txt","r") as rf:
#     with open("File1_copy.txt","w") as wf:
#         for line in rf:
#             wf.write(line)


with open("ScreenShot.png","rb") as rf:
    with open("ScreenShot_copy.png","wb") as wf:
        chunk = 4096
        rf_chunk = rf.read(chunk)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk)
            
        # for line in rf:
        #     wf.write(line)
    
