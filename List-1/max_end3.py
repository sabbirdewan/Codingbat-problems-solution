'''

Given an array of ints length 3, figure out which is larger, the first or last element in the array,
and set all the other elements to be that value. Return the changed array.
'''

def max_end3(nums):
  if nums[0]>nums[len(nums)-1]:
    big=nums[0]
  else:
    big=nums[len(nums)-1]
  for i in range(len(nums)):
    if nums[i] != big:
      nums[i]=big
  return nums

print(max_end3([2, 11, 3]))
