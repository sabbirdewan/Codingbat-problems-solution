'''

Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
'''

def middle_way(a, b):
  temp=a[1:2]+b[1:2]
  return temp

print(middle_way([5, 2, 9], [1, 4, 5]))
