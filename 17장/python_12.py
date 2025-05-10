# Unit 17. while 반복문으로 Hello, world! 100번 출력

i = 0
while i < 100:
  print("Hello, world!")
  i += 1
  
# 형식

# 초기식
# while 조건식:
#   반복할 코드
#   변화식

i = 1
while i <= 100:
  print('Hello, world!',i)
  i += 1
  
# 초깃값 감소시키기

i = 100
while i > 0:
  print("Hello, world!",i)
  i -= 1
  
# 입력한 횟수대로 반복하기

count = int(input("반복할 횟수를 입력하셈: "))

i = 0
while i < count:
  print("Hello world!",i)
  i += 1

# 초기값을 입력받아보기

count = int(input("반복할 횟수 입력: "))

while count > 0:
  print("hello, world!",count)
  count -= 1
  
# 난수 생성해보기

import random # random 모듈을 꼭 가져와야댐 파이썬에선

random.randint(1,6) # 1과 6사이의 랜덤된 수

i = 0
while i != 3:
  i = random.randint(1,6)
  print(i)
  
money = int(input())

while money >= 1350:
  money -= 1350
  print(money)