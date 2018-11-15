'''

Given an int array length 2, return True if it contains a 2 or a 3.
'''

def has23(nums):
  for x in nums:
    if x==2 or x==3:
      return True
  else:
      return False

print(has23([4, 3]) )
