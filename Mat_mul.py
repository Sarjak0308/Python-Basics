import numpy as np
def mul():
   X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x3 matrix
   Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
# result is 3x3
   mult = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterate through rows of X
   for i in range(0,3):
   # iterate through columns of Y
      for j in range(0,3):
       # iterate through rows of Y
         for k in range(0,3):
              mult[i][j] += X[i][k] * Y[k][j]

   for r in mult:
      print(r)


                     

