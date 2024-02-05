def trans():
   X = [[12,7],
    [4 ,5],
    [3 ,8]]

   y = [[0,0,0],
         [0,0,0]]

# iterate through rows
   for i in range(len(X)):
   # iterate through columns
      for j in range(len(X[0])):
          y[j][i] = X[i][j]

   for r in y:
      print(r)
