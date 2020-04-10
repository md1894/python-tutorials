#three statements are there --> if, elif, else
#elif --> else if

age = int(input('enter the age:'))

if(age < 18):
    print('age must be above 18')
    print('govt may take serious action if not sticked to age limit guidelines')
elif(age > 59):
    print('age must not exceed 59 yrs , otherwise not good for health')
    print('go take care of your child')
else:
    print('fine just go ahead')


# to accept a 2D matrix/list from a user and store it
row = int(input('enter row:'))
col = int(input('enter col:'))

matrix_ = [ [ int(input('enter data:')) for x in range(col) ] for y in range(row) ]

for r in range(row):
    for c in range(col):
        print(r,c,matrix_[r][c])

print(matrix_[0][1])

# A basic code for matrix input from user

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()

