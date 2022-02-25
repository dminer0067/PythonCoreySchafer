from tracemalloc import start


nums = [1,8,6,9,15,12,4,2]

mylist = []
print("Using for loop")
# for n in nums:
#     mylist.append(n)
# print(mylist)

#we can write in comprehensive way in one line
print("Using for Comprehensive")
complist1 = [n for n in nums]
print(complist1)

for n in nums:
    mylist.append(n**2)
print(mylist)

complist2 = [n**2 for n in nums]
print(complist2)


even=[]
for n in nums:
    if(n%2==0):
        even.append(n)
print(even)

evenlst = [n for n in nums if n%2 == 0]
print(evenlst)

newlist=[]
for letter in 'abcd':
    for x in range(1,5):
        newlist.append((letter,x))
#print(newlist)

comnewlist = [(letter,x) for letter in 'abcd' for x in range(1,5)]
print(comnewlist)


numbers = [1,3,8,21,18,15,26]
def genefunc(numbers):
    for n in numbers:
        yield n*n
 
mygen = genefunc(numbers)

mygen2 = (n*n for n in numbers)

for i in mygen2:
    print(i)




