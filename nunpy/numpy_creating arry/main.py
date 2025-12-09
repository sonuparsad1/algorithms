import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
arr = np.array((1, 2, 3, 4, 5))

print(arr)
# it give type of array
print(type(arr))
# it give shape of array
print(arr.shape)
#  it give datatype of array
print(arr.dtype)
# it give dimension of array
print(arr.ndim)
# type of array
# 0d array
arr0d = np.array(42)
print(arr0d)
# 1d array
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)
# 2d array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
# 3d array
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print("0d array dimension:", arr0d.ndim)
print("1d array dimension:", arr1d.ndim)
print("2d array dimension:", arr2d.ndim)
print("3d array dimension:", arr3d.ndim)


#  higher dimension array
arr4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
                   [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
print(arr4d)
print("4d array dimension:", arr4d.ndim)

# Higher Dimensional Array
# it define minimum dimension of array
# how it work
# it will convert 1d array into 5d array

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
