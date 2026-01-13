'''import random
from array import arr
from array import *'''
import numpy as np


#finding the square root by different methods.
'''import math
number = int (input("enter a number: "))
sqrt = number**0.5
print("square root : " , sqrt)
print (math.pow(number , 0.5))
print(math.sqrt(number))'''


#smallest divisor

'''num = int  (input("enter a number: "))

for i in range(2, num + 1):
    if num%i ==0 :
        print(i)
        break'''
    

#find the prime no. in the given range of the lower limit and the upper limit.

'''num1 = int (input("enter lower limit: "))
num2 = int (input("enter upper limit: "))

for i in range (num1, num2+1):    
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break
            
        else:
            print(i)'''



#find the prime factors for a given no.

'''n = int (input("enter a number: "))

for i in range(2 , n+1):
    if (n%i == 0):
        for j in range(2, i):
            if (i%j==0):
                break
            else:
                print(i)'''


#find the HCF of the given two numbers.

'''num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

while num2 != 0: 
    temp = num2
    num2 = num1 % num2
    num1 = temp
print(num1)'''


'''a= int (input("enter a no.: "))
b = int (input("enter a no.: "))

val = random.randrange(a,b)

print(val)'''


'''name = input("enter a name: ")

random_name = random.choice(name)

print(random_name)'''



'''n = int(input("Enter a no.: "))

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    a, b = 0, 1
    for n in range(2, n):
        a , b = b , a + b
    print(b)'''
        



'''def sum (n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

a = int(input("enter a number: "))

print(sum(a))

'''


'''def bsearch(arrayName, low, high, a):
    if low > high:
        print("Number not found")
        return
    mid = (low + high) // 2
    if arrayName[mid] == a:
        print("Number found at index:", mid)
        return
    elif a < arrayName[mid]:
        bsearch(arrayName, low, mid - 1, a)
    else:
        bsearch(arrayName, mid + 1, high, a)
'''





'''arrayName = array('i' , [10,20,30, 40 , 47 ,50])


def bsearch(arrayName, low, high, a):
    mid = (low + high) // 2
    if(arrayName[mid] == a):
        print(("number is found at" , mid))
        if(low< high):
            if(a > arrayName(mid)):
                bsearch(arrayName, mid+1, high, a)
            elif(a < arrayName(mid)):
                bsearch(arrayName, low, mid-1, a)
        else:
            print("number not found")




a = int(input("enter a number to search: "))

low = 0
high = len(arrayName)
bsearch(arrayName , low , high - 1 , a)






'''



















'''print(arrayName)

print("---------------------------------")

for x in arrayName:
    print(x)

print("---------------------------------")

print(arrayName[1])
print("---------------------------------")

f = len(arrayName)
print(f)

print("---------------------------------")

arrayName.insert(1 , 47)
print(arrayName)

print(len(arrayName))

print("---------------------------------")

arrayName.remove( 47)
arrayName.remove(47)
print(arrayName)

'''

'''a = int(input("enter a number to searched : "))
for i in range (len (arrayName)):
    if (a == arrayName[i]):
        print("index of the number: " , i)
        break
    else:
        print("not found")
'''




'''numbers = arr.array('i' , [1,2,3,4,5])
print(numbers)

numbers.reverse()
print(numbers)

array2 = arr.array('i' , reversed(numbers))

print(array2)



'''

'''# sorting of an array .

array1 = np.array([10 , 13,97,2,30,45,80])

for k in range(len(array1)):
        for j in range(len(array1) - k - 1):
            if array1[j] > array1[j + 1]:
                t= array1[j]
                array1[j] = array1[j + 1]
                array1[j + 1] = t
print(array1)
'''

    
# write a program that print no. of even and no. of odd no. in a list . (list can be pre-defined)

'''list1 = [1,2,3,4,5,6,7,8,9]
even = 0
odd = 0
for i in list1:
    if i%2 == 0:
         even +=1
    else:
         odd +=1

print(even)
print(odd)



'''




#list 
#extending of the list

'''list1 = [1,2,'VIT' ,5]
list2 = [3,4,6,7]

list1.extend(list2)
print(list1)

list1.remove('VIT')
print(list1)

list1.pop()#last no. will be deleted untill we put a value in the parathesese

print(list1)

print('---------------------------------------')

list1.reverse()
print(list1)

print('---------------------------------------')

list1.sort()
print(list1)


'''



'''num = [10,20,30]
repeat = num*3

print(repeat)


num1 = [ 1,2,3]

num2 = [10,20,30]

print(num == num1)#.  check the list by index to index
print(num1 != num)
print(num2 == num)




'''


'''list1 = [1,2,'VIT' ,5,[40,50,60]]


print(list1)
print(list1[0])
print(list1[3])
print(list1[4])
print(list1[4][0])
print(list1[4][2])

'''




list = [[10,20,30],[40,50,60],[70,80,90]]

for i in list:
    print(*i)


mat1=[]