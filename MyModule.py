print("MyModule Imported...!!")

test = "Test String"

def find_index(tosearch,targer):
    for i,value in enumerate(tosearch):
        if(value == targer):
            print('Found the Target string')
            return i;
    print('Not Found the Target string')
    return -1

