import numpy as np

# a = np.random.normal(15, 2, (10000, 2))
a = np.random.uniform(1, 200, (10000, 2))

print(np.mean(a[:, 0] / a[:, 1]))
print(np.mean(a[:, 1] / a[:, 0]))
