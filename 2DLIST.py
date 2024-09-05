matrix=[[1,3],[5,6],[4,1]]
print(matrix)
#Number Of Rows
print(len(matrix))

#Number of Columns
print(len(matrix[0]))

print(matrix[1][0])


matrix1=[[3,4,5],[7,8,9],[1,2,3],]

#Number of Rows
print(len(matrix1))

#Number of Columns
print(len(matrix1[1]))

print(matrix1[0][0])


for row in range(0,len(matrix1)):
    for column in range(0,len(matrix1[1])):
        print(matrix1[row][column], end=" ")
    print("\n")


rows=int(input("Enter the number of rows."))
columns=int(input("Enter the number of columns."))
a=[]
for row in range(rows):
    temp=[]
    for column in range(columns):
        h=int(input("Enter your elements"))
        temp.append(h)
    a.append(temp)
for row in range(rows):
    for column in range(columns):
        print(a[row][column], end=" ")
    print("\n")

matrixa=[[1,2],[4,5]]
matrixb=[[6,7],[8,9]]
additionresult=[[0,0],[0,0]]
substractionresult=[[0,0],[0,0]]
for i in range(0,2):
    for j in range(0,2):
        additionresult[i][j]=matrixa[i][j]+matrixb[i][j]
        substractionresult[i][j]=matrixa[i][j]-matrixb[i][j]


for row in range(rows):
    for column in range(columns):
        print(additionresult[row][column], end=" ")
    print("\n")
for row in range(rows):
    for column in range(columns):
        print(substractionresult[row][column], end=" ")
    print("\n")

mresult=[[0,0],[0,0]]
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            mresult[i][j]=mresult[i][j]+(matrixa[i][k]*matrixb[k][j])
for row in range(rows):
    for column in range(columns):
        print(mresult[row][column], end=" ")
    print("\n")

