# if 조건문으로 특정 조건일때 코드 실행하기

# if 조건문 사용하기

# if 조건식:
#   코드

x = 10
if x == 10:
  print('10입니다') # 들여쓰기 필수, 그리고 "=" 이 아니고 "==" 을 써야한다
  

x = 10
if x == 10:
  pass # pass는 아무일도 하지않고 넘어간다

x = 10
if x == 10:
  print('x에 들어있는 숫자는')
  print('10입니다')

# 근데 만약에
x = 10
if x == 10:
  print('x에 들어있는 숫자는')
print('10입니다') # 이친구는 들여쓰기가 되어있지않기때문에 if문과 상관없는 코드가 되었음

# 중첩 if문 사용해보기

x = 20
if x >= 10:
  print('10이상입니다')
  
  if x == 15:
    print('15입니다')
    
  if x == 20:
    print('20입니다')
  
# 사용자가 입력한 값에 if조건문 사용하기

x = int(input()) # 입력받은 값을 변수에 저장

if x == 10:
  print('10입니다')
  
if x == 20:
  print('20입니다')
  
price = int(input())
c_name = str(input())

if c_name == 'Cash3000':
  print(price - 3000)
  
if c_name == 'Cash5000':
  print(price - 5000)