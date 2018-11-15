'''
Given a string and a non-negative int n,
return a larger string that is n copies of the original string.
'''

def string_times(str, n):
  if n > 0: 
    return n*str
  if n==0: 
    return ""

print(string_times('Hi', 3))
