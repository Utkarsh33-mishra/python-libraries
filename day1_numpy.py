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

# import numpy as np
# arr = np.array([1,2,3,4,5,6]) # output (6,) means . 6 element  >. 1 dimension

# print(arr.shape)
# print(arr.reshape(2,3)) # means 2 rows and 3 column ,element will be 6
# print(arr.reshape(3,2)) # 3 rows and 2 column
# print(arr.reshape(6)) # 6 element in 1 D
#  total element always remain same only their reprentation shape will change
# print(arr.reshape(2,-1))
# print(arr.reshape(3,-1)) # 3 rows and for column 6%3 = 2 column
# print(arr.reshape(-1,2)) #row = ?  and 2 column for row 6%2 = 3

#  FLATTERING : CONVERTING A Multu_dimensional array in 1 d array

# import numpy as np

# arr = np.array([1,2,3,4,5,6])

# flat = arr.flatten()
# flat[0] = 100  # in this outputmemory don't change

# print(flat)
# print(arr)

# import numpy as np
# arr = np.array([
#     [1,2,3],
#     [3,4,5]
# ])

# rav = arr.ravel()
# rav[0] = 89
# print(rav)
# print(arr)

# import numpy as np
# arr = np.array([
#     [1,2,3,],
#     [4,5,6]
# ])

# flat = arr.flatten()
# flat[2] = 9
# print(flat)
# print(arr)

# rav = arr.ravel()
# rav[1] = 77
# print(rav)
# print(arr)

#  Matrix operation

# import numpy as np         # matrix operation on 1 D
# a= np.array([10,20,30])
# b = np.array([1,2,3])

# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a/b)

# import numpy as np

# a= np.array([         # matrix op on 2D
#     [1,2],
#     [3,4]
# ])

# b = np.array([
#     [5,6],
#     [7,8]
# ])

# print(a+b)
# print(a-b)
# print(a*b)
# print(b%a)
# print(a/b)

# import numpy as np

# a = np.array([
#     [[1,2],[3,4]],
#     [[5,6],[7,8]]
# ])

# b = np.array([
#     [[10,20],[30,40]],
#     [[50,60],[70,80]]
# ])

# print(a+b)
# print(a-b)
# print(a*b)
# print(b/a)
# print(b%a)

# BROADCASTING  ; NUMPY AUTOMATICALLY ARRANGE ACCORDING TO SMALLER ARRAY & PERFORM OP
# import numpy as np
# a = np.array([
#     [10,20],
#     [30,40]
# ])

# b = np.array([1,2]) # here b as being applied on each row
# print(a+b)

# a = np.array([10,20,30])
# b = 2

# print(a*b)

# UNIversal function

# import numpy as np
# a = np.array([1,-2,3,-5,6])
# print(np.sqrt(a))
# print(np.square(a))
# print(np.exp(a))
# print(np.abs(a))
# print(np.sin(a))
# print(np.cos(a))
# print(np.log(a))

# MEAN,MEDIAN ,MODE
# import numpy as np
# a= np.array([10,20,30,40,50])
# print(np.mean(a))
# print(np.median(a))
# print(np.std(a))

import numpy as np 
# a = np.array([[
#     [10,20,30],
#     [40,50,60]
# ]])

# print(np.mean(a))
# print(np.std(a))
# print(np.sum(a))
# print(np.min(a))
# print(np.max(a))
# these are going to op on whole array.

# a = np.array([
#     [10,20,30],
#     [40,50,60]
# ])

# print(np.mean(a,axis= 0))
# print(np.mean(a,axis = 1))
# print(np.median(a,axis = 1))
# print(np.median(a,axis = 0))

# a = np.array([

#     [[1,2], [3,4]],
#     [[5,6], [7,8]]
# ])
# # print(np.mean(a))
# # print(np.mean(a,axis = 1))
# print(np.mean(a,axis = 0))

# # standard deviation
# a = np.array([
#     [10,10,10],
#     [20,20,20]
# ])

# print(np.std(a))# np.std(a) -- onemean for everything
# print(np.std(a,axis =0))# mean separately for each column
# print(np.std(a,axis =1)) # mean separatley for each row

# RANDOM MODULE
# import numpy as np
# a = np.random.randint(10,50,(2,3)) # random matrix
# print(a)
# import numpy as np
# a = np.random.rand(3) # 3 random decimal no bw 0 and 1
# print(a)
#
# a = np.random.randint(1,10,5) # integer value multiple
# print(a)

# MATRIX MULTIPLICATION
# import numpy as np
# A = np.array([
#     [1,2],
#     [3,4]
# ])
# # Element wise multiplication
# B = np.array([
#     [5,6],
#     [7,8]
# ])
# print(A@B)

# DOT PRODUCT
# import numpy as np
# a = np.array([3,4,5])
# b = np.array([2,3,4]) # MULTIPLY CORROSPONDING ELEMENT THEN ADD
# print(np.dot(a,b))

# cluster1 = np.random.normal(5,1,(5,2))
# print(cluster1)

a = np.arange(1,10,2)
print(a)
# arrange = (start,stop,jump)