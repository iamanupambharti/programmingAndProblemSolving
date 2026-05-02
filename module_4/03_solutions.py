#Find GCD:
## Method 1:

# import math
# print("The GCD of 60 and 48 is: ", end="")
# gcd=math.gcd(60,48)
# print(gcd)

##Method 2: Euclidean Algorithm 

# def GCD(x,y):
#     while(y):
#         x,y=y, x%y
#     return x

# a=60
# b=48
# print("THe GCD of 60 and 48 is: ",end="")
# print(GCD(60,48))

##Method 3:Recursive method

def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

print(GCD(60,48))