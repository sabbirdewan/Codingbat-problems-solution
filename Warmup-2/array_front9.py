'''

Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.
'''

def array_front9(nums):
  count=1
  for x in nums[:4]:
    if x==9:
      return True
  return False

print(array_front9([1, 2, 3, 4, 5]))
