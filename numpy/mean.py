import numpy as np

values = np.arange(12).reshape(4,3)
print(values,'\n')



print(np.mean(values),'\n')
print('axis = 0 calculate means value over each column')
print(np.mean(values, axis=0),'\n')

print('axis =1 calculate means value over each rows')
print(np.mean(values, axis=1),'\n')

