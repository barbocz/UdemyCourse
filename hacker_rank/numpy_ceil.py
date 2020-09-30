import numpy


# def arrays(arr):
#     return(numpy.array(arr[::-1], float))
#
# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)

# n, m = map(int, input().split())
# a = (numpy.array([input().split() for _ in range(n)], dtype=int) )
# print(numpy.prod(numpy.sum(a,axis=0) ))


# n, m = map(int, input().split())
# a = (numpy.array([input().split() for _ in range(n)], dtype=int) )
# print(numpy.max(numpy.min(a,axis=1) ))

# n, m = map(int, input().split())
# a = (numpy.array([input().split() for _ in range(n)], dtype=int) )
# print(numpy.prod(numpy.sum(a,axis=0) ))

# print(numpy.array(input().split(),int).reshape(3,3))

# n, m = map(int, input().split())
# array = numpy.array([input().strip().split() for _ in range(n)], int)
# print (array.transpose())
# print (array.flatten())

# a, b, c = map(int,input().split())
# arrA = numpy.array([input().split() for _ in range(a)],int)
# arrB = numpy.array([input().split() for _ in range(b)],int)
# print(numpy.concatenate((arrA, arrB), axis = 0))

# nums = tuple(map(int, input().split()))
# print (numpy.zeros(nums, dtype = numpy.int))
# print (numpy.ones(nums, dtype = numpy.int))

print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))
print (numpy.identity(3))

