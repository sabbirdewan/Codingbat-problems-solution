'''


Given an array of ints, return a new array length 2 containing the first and
last elements from the original array. The original array will be length 1 or more.
'''

def make_ends(nums):
  temp=nums[0:1]+nums[-1:]
  return temp
print(make_ends([1, 2, 3, 4]))
