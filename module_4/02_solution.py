# Smallest Divisor

## Method 1: Program 1:

# number=int(input("Enter the Number: "))
# for i in range(2,number+1):
#     if number%i==0:
#         print("The smallest divisor for ", number, " is ", i)
#         break

## MEthod 2: Program 2:
n= int(input("Enter an Integer: "))
a=[]

for i in range(2,n+1):
    if (n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor is:" , a[0] )