import numpy as np

# transpose means: make the rows columns and the columns rows
a = np.arange(60).reshape(10, 6)
print(f"array is: \n {a}", '\n')
print(f"this is the transpose: \n {a.T}")
print('+++++++++++++++++++++++++++', '\n')
b = np.arange(60).reshape(6, 5, 2)
print(f"this is new array with 2D:\n {b} ", '\n')

print(f"let's transpose it : \n {b.transpose()}")
print(f"the shape become{b.transpose().shape}")