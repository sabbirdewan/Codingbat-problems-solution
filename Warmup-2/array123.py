'''
Given an array of ints,
return True if the sequence of numbers 1, 2, 3
appears in the array somewhere.
'''

def array123(nums):
  temp=[1,2,3]
  if len(nums) <3:
    return False 
  for i in range(len(nums)-2):
    if(nums[i:i+3]==temp):
      return True
  else:
      return False

print(array123([1, 1, 2, 1, 2, 3]))
