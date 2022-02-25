#print("First Module name is : {}".format(__name__))

print("This statement will always get executed")

def main():
    print("First Module's Main Method")
    #pass

if __name__ == '__main__':
    main()
# else:
#     print("Run from Import")