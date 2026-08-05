# import numpy as np

# print("Nmpy version:", np.__version__)


# arr = np.array([10,20,30,40])

# print(arr)
# print(type(arr))

# import numpy as np

# arr = np.array([1,2,3,4,5])

# print(arr)

# import numpy as np

# arr = np.array([
#     [1,2,3],
#     [4,5,6],
# ])

# print(arr)

# import numpy as np

# arr = np.array([
#     [
#         [1,2],
#         [3,4]
#     ],
#     [
#         [5,6],
#         [6,7]
#     ]
# ])

# print(arr)

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

print(arr.ndim)  # Number of dimension
print(arr.shape) # Row and column
print(arr.size) # Total element
print(arr.dtype) # Data type