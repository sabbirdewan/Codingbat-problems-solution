'''

Given a non-empty string like "Code" return a string like "CCoCodCode".

'''

def string_splosion(str):
  if str != "":
    result=""
    for i in range(len(str)):
      result+=str[:i+1]
    return result

print(string_splosion('There'))
