import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],\
			[10, 11, 12], [13, 14, 15]])

A1 = np.arange(1,16).reshape(5, 3)

print(A.ndim, A.shape, A.dtype.name, A.size, A.itemsize, A.data)
print(A1.ndim, A1.shape, A1.dtype.name, A1.size, A1.itemsize, A1.data)

O1 = np.ones((5, 3))
Z1 = np.zeros((5, 3))
E1 = np.empty((5, 3))
e1 = np.eye(5)
print("O1, Z1, E1, e1", O1, Z1, E1, e1)