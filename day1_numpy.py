# import numpy as np

# print("Nmpy version:", np.__version__)


# arr = np.array([10,20,30,40])

# print(arr)
# print(type(arr))

# import numpy as np

# arr = np.array([1,2,3,4,5])  # 1D array

# print(arr)

# import numpy as np 
                             # 2D array
# arr = np.array([
#     [1,2,3],
#     [4,5,6],
# ])

# print(arr)

 # 3D array

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

# use of shape,ndim,size,dtype
 # import numpy as np

# arr = np.array([[1,2,3],[4,5,6]])

# print(arr.ndim)  # Number of dimension
# print(arr.shape) # Row and column
# print(arr.size) # Total element
# print(arr.dtype) # Data type

# Indexing 

# import numpy as np
# arr = np.array([1,2,3,4,5])

# print(arr[0])
# print(arr[-1])

# arr = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(arr[0,1])
# print(arr[1,2])

# arr = np.array([
#     [[1,2],[3,4]],
#     [[5,6],[7,8]]
# ])

# print(arr[0,1,1])
# print(arr[1,1,0])

#  SLICING
# import numpy as np
# arr = np.array([1,2,3,4,5])

# print(arr[1:4])  # index 1 to 3
# print(arr[:3])   # begining to index 2
# print(arr[::2])  # every 2nd element jump python assume start itself from 0
# print(arr[1:])   # index 1 to end
# print(arr[:-1])  #begining to one before last

# import numpy as np
# arr = np.array([
#     [1,2,3],
#     [3,4,5]
# ])

# print(arr[:,1])  # All rows, column1
# print(arr[0,:])  # Row 0, all columns
# print(arr[:,0:2]) # All rows,column  0 and 1
# print(arr[1,:])   # Row 1, All columns

#  RESHAPING 

import numpy as np
arr = np.array([1,2,3,4,5,6]) # output (6,) means . 6 element  >. 1 dimension

# print(arr.shape)
# print(arr.reshape(2,3)) # means 2 rows and 3 column ,element will be 6
# print(arr.reshape(3,2)) # 3 rows and 2 column
# print(arr.reshape(6)) # 6 element in 1 D
#  total element always remain same only their reprentation shape will change
print(arr.reshape(2,-1))
print(arr.reshape(3,-1)) # 3 rows and for column 6%3 = 2 column
print(arr.reshape(-1,2)) #row = ?  and 2 column for row 6%2 = 3