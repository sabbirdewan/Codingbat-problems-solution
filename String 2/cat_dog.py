def cat_dog(str):
  dog_count=0
  cat_count=0
  for i in range(len(str)-2):
    if str[i:i+3]=="dog":
      dog_count+=1
    if str[i:i+3]=="cat":
      cat_count+=1
  if dog_count==cat_count:
    return True 
  else:
    return False
print(cat_dog('catxdogxdogxcat'))
