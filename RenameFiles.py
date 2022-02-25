import os

path = os.chdir("E:\StudyRelated\Python-CoreySchafer\Fileoperation")
#print(os.getcwd())

for f in os.listdir():
    #print(f)
    f_name,f_ext = (os.path.splitext(f))
    f_title,f_course,f_num = f_name.split("-")
    
    
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)  #f_num.strip()[1:] used to remove # from string #zfill method used for fill 0
    
    #print("{}-{}{}".format(f_num,f_title,f_ext))
    new_name = "{}-{}{}".format(f_num,f_title,f_ext)
    #print(new_name)
    
    os.rename(f,new_name)
    
    