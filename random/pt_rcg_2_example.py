# 例題 p32
import numpy as np
from scipy import linalg as la

# x1 = np.array([-5., 0.])
# x2 = np.array([1., 4.])
# x3 = np.array([-2., 1.])
# x4 = np.array([-2., 3.])
x1 = np.array([2., -1.])
x2 = np.array([2., -3.])
x3 = np.array([5., 0.])
x4 = np.array([-1., -4.])

# 1.
ave = (x1 + x2 + x3 + x4) / 4 # ave == 0
x1 -= ave
x2 -= ave
x3 -= ave
x4 -= ave
print(ave)
X = np.matrix([x1, x2, x3, x4])
C = (X.T * X) / 4
print(C)

# 2.


# 3.
eig_val, eig_vec = la.eig(C)
# print(eig_val)
# print(eig_vec)
max_eig_val = max(eig_val)
print(f'max_val: {max_eig_val}')

TMP = np.matrix([[-2., 2.], [2., -2.]])
print()
print((TMP.T * TMP) / 2)