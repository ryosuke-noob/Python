import numpy as np
from scipy import linalg as la

# 線形回帰
D = np.matrix([[0,0,1], [0,1,1],[0,2,1],[0,3,1],[1,0,1],[1,1,1]\
               ,[1,2,1],[1,3,1],[2,0,1],[2,1,1],[2,2,1],[2,3,1]])
y = np.matrix([1,3,2,3,1,4,5,4,4,5,4,7])
y = y.T
A = D.T * D
w = la.inv(A) * D.T * y

print(w)
