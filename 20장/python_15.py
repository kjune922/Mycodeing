# Unit 20. FizzBuzz 문제풀어보기

# 예시
# 1에서 100까지 출력
# 3의 배수는 Fizz출력
# 5의 배수는 Buzz 출력
# 3과 5의 배수는 FizzBuzz 출력

for i in range(1,101):
  print(i)
  
for i in range(1,101):
  if(i % 3 == 0 and i % 5 == 0):
    print("FizzBuzz")
  if(i % 3 == 0):
    print("Fizz")
  elif(i % 5 == 0):
    print("Buzz")
  else:
    print(i)
    
# 코드 ㅈㄴ단축해보기

for i in range(1,101):
  print("Fizz" * (i%3==0) + "Buzz" * (i%5==0) or i) # i를 3으로 나눈 나머지가 0이 True일때만 Fizz출력, 아니면 아무것도 출력안함
  
print("Fizz"+"Buzz")
print("Fizz"*True)
print("Fizz"*False)