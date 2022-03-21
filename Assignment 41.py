# Write a program which can map() to make a list whose elements 
# are square of elements in [1,2,3,4,5,6,7,8,9,10].
def square(n):
  return n * n
nums = [1,2,3,4,5,6,7,8,9,10]
result = map(square, nums)
print(list(result))