# Program to add two matrices using list comprehension

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for f in result:
   print(f)
   
   
   # Program to multiply two matrices using list comprehension


Z = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]


K = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result1 = [[sum(a*b for a,b in zip(Z_row,K_col)) for K_col in zip(*K)] for Z_row in Z]

for r in result1:
   print(r)
