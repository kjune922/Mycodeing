# Unit 14. else를 사용해서 두 방향으로 분기하기

# else 사용하기

x = 5
if x == 10:
  print('10입니다')
else:
  print('10이 아닙니다')

x = 5
if x == 10:
  print('10입니다.')
else:
  print('x에 들어있는 숫자는')
  print('10이 아닙니다.')
  
if True:
  print('참')
else:
  print('거짓')

if False:
  print('참')
else:
  print('거짓')

if None:
  print('참')
else:
  print('거짓')
  
# 참고로 숫자는 0이면 거짓, 0이아니면 다 참이다
# 문자열은 빈 문자열은 거짓, 내용이 있으면 다 참

x = 10
y = 20

if x == 10 and y == 20:
  print('참')
else:
  print('거짓')
  
if x > 0:
  if x < 20:
    print('20보다 작은 양수입니다')
    
# 위의 중첩 if문을 한줄로 줄일수있다

if x > 0 and x < 20:
  print('0보다 크고 20보다 작은 양수')
  
# 파이썬에선 이걸 한번더 가능

if 0 < x < 20:
  print('0보다 크고 20보다 작은 양수')


kor,eng,math,sci = input().split()
k = int(kor)
e = int(eng)
m = int(math)
s = int(sci)
if (k < 0 or k > 100) or (e < 0 or e > 100) or (m < 0 or m > 100) or (s < 0 or s > 100):
  print('잘못된 점수')
else:
  total = k + e + m + s
  if total / 4 >= 80:
    print('합격')
  else:
    print('불합격')