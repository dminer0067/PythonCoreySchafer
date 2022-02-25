from operator import index
from pickle import TRUE

#List
frontend = ["HTML/CSS","Angular","Java Script","React"]

backend = ["Php","Asp.net","Java","R Programming","Swift"]

print(frontend)
type(frontend)

print(frontend[1:3])
print(len(backend))
frontend.append("flutter")
print(frontend)



lst1 = ['Item1','Item2','Item3']
lst2 =['LI1','LI2']

#Extend will extend the lis items
lst1.extend(lst2)
print(lst1)
#append will append entire list 
lst1.append(lst2)
print(lst1)
#emove specific value it accepts only one argument
lst1.remove('LI1')
print(lst1)
#remove lastvalue
lst1.pop()
print(lst1)

lst1.reverse()
print(lst1)

print("Before Sort : ",frontend)

frontend.sort()
print("After Sort : ",frontend)


frontend.sort(reverse=True)

print("Reverse Sort :",frontend)

asc = sorted(backend)

print(backend)
print(asc)

#sorted() - Sorted version of the list without sorting original list
#Sort() - It will modify the original list whle soting

numlist = [45,96,12,6,48]

print(sum(numlist))

print(index(2 in numlist))
print(45 in numlist)

for index,item in enumerate(numlist,start=3):
    print(index,item)


subjects = ['History','Science','Maths','Social Science']

str = ' - '.join(subjects)

print(str)

split = str.split(' - ')

print(split)

#list are mutable Tuples are not mutable
print("List")
newlist1 = ['History','Science','Maths','Social Science']
newlist2 = newlist1
newlist1[0] = 'Art'
print(newlist1)
print(newlist2)
print("-----------------------------------------------------------")

print("Tuples")
tup1 = ('History','Science','Maths','Social Science')
tup2 = tup1

print(tup1)
print(tup2)

#tup1[0] = 'Art'  Tuples are immutable so can't assign it won't work.

print(tup1)
print(tup2)
print("-----------------------------------------------------------")




#Sets

set1 = {'History','Science','Maths','Social Science'}

set2 = {'History','Science','Art','Social Science'}
print(set1.intersection(set2))

print(set1.difference(set2))

print(set1.union(set2))
