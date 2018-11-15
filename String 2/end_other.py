def end_other(a, b):
  a=a.lower()
  b=b.lower()
  length=min(len(a), len(b)) #find short strign and min length
  if a[-length:] == b or b[-length:]==a: # if a.endswith(b) or b.endswith(a): works same 
    return True 
  else:
    return False 
print(end_other('AbC', 'HiaBc'))
