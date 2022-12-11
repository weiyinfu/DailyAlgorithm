from scipy.optimize import linear_sum_assignment
import numpy as np
from scipy.sparse import csr

a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 9]])
x, y = linear_sum_assignment(a, maximize=True)
print(x, y)
print(a)
print(a[x, y])

a = csr.csr_matrix(([1, 2, 3], (0, 1, 2), (0, 1, 2)))
print(a)
x, y = linear_sum_assignment(a, maximize=True)
print(a[x, y])
