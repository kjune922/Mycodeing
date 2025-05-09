# Unit 16. for와 range 사용하기

# 예시
# for 변수 in range(횟수):
#   반복할 코드

for i in range(100):
  print('Hello world!')

# 이처럼 for 반복문은 반복 횟수가 정해져 있을 때 주로 사용한다 >> 반복할 코드로 순환한다 >> 루프

for i in range(100):
  print('Hello, world!', i)

# 시작하는 숫자와 끝나는 숫자 지정해보기

for i in range(5, 12):  # 5부터 11까지 반복
  print('Hello, world!',i)
  
# 증가폭 사용해보기

for i in range(0,10,2): # 0부터 8까지 2씩증가
  print("Hello, world!",i)
  
for i in range(10,0,-1):
  print('Hello, world!',i)
  
# 입력한 횟수대로 반복하기

count = int(input('반복할 횟수 입력: '))

for i in range(count):
  print('Hello, world!',i)
  
# for에 range대신 시퀀스 객체를 넣어도된다

a = [10,20,30,40,50]

for i in a:
  print(i)
  
# 문자열도 가능, 뒤바꿔서 출력해보기
for letter in ('Python'):
  print(letter)

for letter in reversed('Python'):
  print(letter)
  
count = int(input())

for i in range(count):
  print('i의 값은',end=' ')
  print(i)
  
num = int(input())

for i in range(1,10):
  result = num * i
  print(num,"*",i,"=",result)