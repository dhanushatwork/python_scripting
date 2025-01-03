#The try block will generate an error, because x is not defined:
try:
    a = 10
    b = 0
    x = a/b
    print(x)
except:
  print("An exception occurred")