'''

Given an array of ints length 3, return an array with the elements
"rotated left" so {1, 2, 3} yields {2, 3, 1}.
'''

def rotate_left3(nums):
  temp=[]
  if len(nums)<3:
    return False
  else:
    temp=nums[1:]+nums[:1]
    return temp
print(rotate_left3([5, 11, 9]))
