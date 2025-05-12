# Unit 18. break, continue로 반복문 제어하기

# break는 for나 while문법에서 제어흐름을 벗어나기 위해 사용, 루프를 완전히 중단한다
# continue는 break와 다르게 제어흐름은 유지하고, 코드의 실행만 건너뛴다

i = 0
while True:
  print(i)
  i += 1
  if i == 100:
    break
  
for i in range(1000):
  print(i)
  if i == 100:
    break
  
# for에서 continue로 코드실행 건너뛰기

for i in range(100):
  if i % 2 == 0:
    continue # continue로 2로나눴을때 나머지가 0인 짝수들을 건너뛰고 홀수만 출력
  print(i)
  
i = 0
while i < 100:
  i += 1
  if i % 2 == 0:
    continue
  print(i)

# pass
# for,while의 반복문에서 아무 일도 하지않지만, 형태는 유지하고싶다면 pass 사용

for i in range(10):
  pass

# while True: 무한루프
#   pass

# 입력한 횟수대로 반복

count = int(input("반복할 횟수를 입력하세요: "))

i = 0
while True:
  print(i)
  i += 1
  if i == count:
    break
  
# 입력한 숫자까지 홀수 출력
count = int(input("반복할 횟수 입력: "))

i = 0
for i in range(count+1):
  if i % 2 == 0:
    continue
  print(i)
  
  