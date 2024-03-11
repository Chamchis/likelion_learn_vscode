import numpy as np
print(np)

arr1 = np.array([1,2,3,4,5])
# print(arr1)
# print(type(arr1))

arr2 = np.array([[1,2,3],
                [4,5,6]])
# print(arr2)
# print(arr1.shape)
# print(arr2.shape)
# print(arr2.reshape(3,2))
# print(arr2.reshape(6,1))
# print(arr2.reshape(1,6))

# print(arr2.reshape(-1,3))
# print(arr2.reshape(-1))
print(arr2.reshape(1,3,-2))

# arr1 = np.array([10,42,65])
# arr2 = np.array([105,92,5])
# print(arr1 + arr2)

# a1 = [10,42,65]
# a2 = [105,92,5]
# print(a1 + a2)
# print(arr1 * arr2)

# arr = np.array([1,2,3,4,5])
# print(np.mean(arr), np.std(arr))

# nums = [i for i in range(10000000)]
# list_mean = sum(nums)/len(nums)
# print(list_mean)
# np_mean = np.mean(np.array(nums))
# print(np_mean)

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr + 1)
# print(arr + np.array([1051,293,501]))

# a = np.array([[1,2],
#               [3,4,]])
# b = np.array([[10,20],
#               [30,40,]])

# print(a+b)
# print(a*b)
# print(np.dot(a,b))

# print(np.int8)
# print(2**8)

# print(np.float16)