a,b = map(int,input().split())

for i in range(a,b+1):
  if a > b:
    break
  if(i % 5 == 0 and i % 7 == 0):
    print("FizzBuzz")
  elif(i % 5 == 0):
    print("Fizz")
  elif(i % 7 == 0):
    print("Buzz")
  else:
    print(i)