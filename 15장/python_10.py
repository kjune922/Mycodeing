# Unit 15. elif 를 사용하여 여러 방향으로 분기하기
# 한마디로 파이썬에선 else if를 elif라고 함

x = 20
if x == 10:
  print('10입니다.')
elif x == 20:
  print('20입니다.')
  
# if, elif, else 다 써보기

x = 30
if x == 10:
  print('10임')
elif x == 20:
  print('20임')
else:
  print('10도 20도아님')
  
# 참고로 elif앞에 else가오면 문법오류

button = int(input())

if button == 1:
  print("콜라")
elif button == 2:
  print("사이다")
elif button == 3:
  print("환타")
elif button == 4:
  print("웰치스")
else:
  print('잘못된 입력')
  
age = int(input())
balance = 9000 # 교통카드 잔액

if age >= 7 and age <= 12:
  balance = balance - 650
elif age >= 13 and age <= 18:
  balance = balance - 1050
elif age >= 19:
  balance = balance - 1250
  
print(balance)