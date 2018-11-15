def big_diff(nums):
  small=min(nums) # can use minimum=min(minimum,nums[i]) where first minimum is first value of list
  big=max(nums)    #can use maximum=max(maximum,nums[i]) where first maximum is first value of list
  return big-small
  
