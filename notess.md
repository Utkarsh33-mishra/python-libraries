l## What is NumPy?
**NumPy (Numerical Python)** is a Python library used for **fast numerical computing**.
It provides a powerful **N-dimensional array (`ndarray`)** to store and process data efficiently.

Example:
```python
import numpy as np

arr = np.array([10, 20, 30])
print(arr)
```

---

## Why NumPy Exists?

Python lists are flexible but become **slow and memory-intensive** when working with large amounts of numerical data.

NumPy was created to:
- Perform calculations faster.
- Use less memory.
- Handle large datasets efficiently.
- Support multi-dimensional arrays.
- Provide built-in mathematical functions.

---

## Python List vs NumPy Array

| Python List | NumPy Array |
|-------------|-------------|
| Stores different data types | Usually stores same data type |
| Slower | Much faster |
| Uses more memory | Uses less memory |
| Limited mathematical operations | Supports vectorized operations |
| Part of Python | Requires NumPy library |

Example:

```python
# Python List
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
# Output: [1, 2, 3, 4, 5, 6]
```

```python
# NumPy Array
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
# Output: [5 7 9]
```

---

## Advantages of NumPy

- Fast execution
- Memory efficient
- Easy mathematical operations
- Supports 1D, 2D, and ND arrays
- Rich collection of built-in functions
- Widely used in Data Science, Machine Learning, and AI

---

## Speed

NumPy is much faster than Python lists because:
- It is implemented in **C**.
- Data is stored continuously in memory.
- Operations are performed on the whole array at once (**vectorization**).

Example:

```python
arr = np.array([1, 2, 3])

print(arr * 2)
# Output: [2 4 6]
```

---

## Memory Efficiency

NumPy arrays use less memory because:
- All elements have the same data type.
- Data is stored in contiguous memory.
- No extra memory is needed for storing object information.

Result:
- Less RAM usage
- Faster processing
- Better performance for large datasets

---

## Key Points (Interview)

- NumPy = Numerical Python.
- Main object = `ndarray`.
- Faster than Python lists.
- Uses less memory.
- Supports vectorized mathematical operations.
- Foundation of Pandas, SciPy, Matplotlib, and many ML libraries.