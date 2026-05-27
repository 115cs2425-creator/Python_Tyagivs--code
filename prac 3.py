import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
print(arr.sum(axis=0))  # Sum of each column
print(arr.sum(axis=1))  # Sum of each row
arr.flat
for item in arr.flat:
    print(item)
    print(arr.ndim)
    print(arr.nbytes)
    one = np.array([3,4,7,654])
    print(one.argmax())
    print(one.argmin())
    print(one.argsort())
    print([324,34]+[34,546]) 





print(np.count_nonzero(arr))
import sys
py_ar = [0,4,55,2]
np_ar = np.array(py_ar)
print(sys.getsizeof(1)*len(py_ar))
print(np_ar.itemsize * np_ar.size)