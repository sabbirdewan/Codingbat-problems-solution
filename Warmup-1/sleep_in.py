def sleep_in(weekday, vacation):
  if not weekday or vacation: 
    return True 
  else:
    return False

print(sleep_in(False, False))
#sleep_in(True, False)
#sleep_in(False, True)
#sleep_in(True, True)
