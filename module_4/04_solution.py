#Generate prime numbers


## MEthod 1 :
x= eval(input("Enter number: "))
while x!=1:

 for i in range (2,x+1):
  if x%i==0:
   print(i)
   x=x//i
   break