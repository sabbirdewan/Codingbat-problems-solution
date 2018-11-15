def count_code(str):
  count=0
  for i in range(len(str)-3): #last position of loop is len-3
    if str[i:i+2]=="co": #check first two character of "code"
        #skip checking of third character of "code"
      if str[i+3]=="e":  #check last character of "code"
        count+=1
  return count

print(count_code('AAcodeBBcoleCCccoreDD'))
