import numpy

# x= numpy.array([[1,2],[4,5]])
# y= numpy.array([[7,8],[9,10]])

# print("The element wise addition of matrix is : ")
# print(numpy.add(x,y))

# print("The element wise substraction of matrix is : ")
# print(numpy.subtract(x,y))

# print("The element wise division of matrix is : ")
# print(numpy.divide(x,y))



mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[7,8,9],[6,5,4],[3,2,1]]
mat3=[[0,0,0],[0,0,0],[0,0,0]]

# Printing the matrix 
# for i in range (len(mat1[0])):
#     for j in range (len(mat1)):
#         print(mat1[i][j] , end=" " )
#     print()

#matrix addition
for i in range (len(mat3[0])):
    for j in range(len(mat3[1])):
         mat3[i][j] = mat1[i][j] + mat2[i][j]

print ()



# Matrix multiplication 
for i in range (len(mat2[0])):
     for j in range (len(mat2[1])):
        for k in range(len(mat3[0])):
            mat3[i][j]=mat3[i][j]+ mat1[i][k]* mat2[k][j]
        
print()

# Matrix Transpose 
for i in range(len(mat1)):
    for j in range (len(mat1[0])):
        mat3[j] [i] = mat1[i][j]


for i in range (len(mat3)):
    for j in range(len(mat3[0])):
        print(mat3[i][j], end=" ")
    print()