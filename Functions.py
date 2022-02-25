def hello_func():
    return "Hello Python...!"

print(hello_func)
print(hello_func())

hello_func()
hello_func()
hello_func()
hello_func()
print(hello_func())


def hellomsg(greeting,language = 'Python'):    
    return '{},{} '.format(greeting,language)

print(hellomsg('Good morning',language='Java'))
print(hellomsg('Good morning'))