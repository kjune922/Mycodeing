# Unit 33. 클로저 사용하기

# 변수의 사용 범위와 함수를 클로저 형태로 만드는 방법을 알아보자
# 클로저는 어렵다 그러므로 먼저 변수의 사용 범위부터 알아본 뒤에 ㄱㄱ


# 1. 변수의 사용 범위 알아보기
# 파이썬 스크립트에서 변수를 만들면 다음과 같이 함수 안에서도 사용 가능

x = 10 # 전역변수
def foo(): # 지역범위
  x = 20
  print(x) # 지역범위
foo() # 전역범위
print(x)

# 2. 함수 안에서 전역 변수 사용해보기
# global 키워드 사용
x = 10
def foo():
  global x
  x = 20 # x가 전역변수가 되어버린다
  print(x)
  
foo()
print(x)

# 함수 안에서 함수 만들어보기

# def 함수이름1():
  # 코드
  # def 함수이름2():
    # 코드
    
def print_hello():
  hello = "Hello, world!"
  def print_message():
    print(hello)
  print_message() # print_hello()안에서 print_message()를 이렇게 함수를 호출해야함 안하면 정의만하는 꼴이됨

print_hello()

# 지역 변수의 범위

def print_hello():
  hello = "Hello, world!"
  def print_message():
    print(hello) # 바깥쪽 함수의 지역 변수를 사용
  print_message()
print_hello()

# 지역 변수 변경하기

def A():
  x = 10    # A의 지역변수 x
  def B():
    x = 20  # x에 20 할당
  B()
  print(x)
A()

# 이렇게하면 20이나올거같지만 10이 나온다.. 함수의 바깥쪽에있는 x에 20을 할당하고싶으면 "nonlocal" 키워드 사용

def A():
  x = 10
  def B():
    nonlocal x # 이렇게 함수바깥의 지역변수x에 20을 할당하고싶다 >> nonlocal사용
    x = 20
  B()
  print(x)
A()

# nonlocal이 변수를 찾는 순서

def A():
  x = 10
  y = 100
  def B():
    x = 20
    def C():
      nonlocal x # 여기서 nonlocal을 했으니 가장가까운 바깥함수인 B에서 x를 찾아서 쓴다
      nonlocal y
      x = x + 30 # 그래서 여기서 x가 10이아니고 20이되어서 결과가 50이나옴
      y = y + 300 # y는 B에 y가없기때문에 A까지올라가서 y를 들고온다
      print(x)
      print(y)
    C()
  B()
A()

# global로 전역 변수 사용하기

x = 10
def A():
  def B():
    x = 20
    def C():
      global x # 전역변수를 이제부터 내가 쓰겠다
      x = x + 30 # x가 10이된다
      print(x)
    C()
  B()
A()

# 이제 함수를 클로저 형태로 만들어보자

# 지역변수 a,b를 사용해서 a * x + b를 계산하는 함수 mul_add를 만들고, 함수 mul_add 자체를 반환해보자

def calc():
  a = 3
  b = 5
  def mul_add(x):
    return a * x + b # 함수 바깥쪽에 있는 지역 변수 a,b를 사용해서 계산
  return mul_add # mul_add 함수자체를 반환
c = calc()
print(c(1),c(2),c(3),c(4))

# 함수 자체를 반환할떄는 "()"이거 붙이면안됨 

# lambda로 클로저 만들어보기

def calc():
  a = 3
  b = 5
  return lambda x: a * x + b # 람다표현식 반환

c = calc()
print(c(1),c(2))

# 클로저의 지역 변수 변경하기

def calc():
  a = 3
  b = 5
  total = 0
  def mul_add(x):
    nonlocal total
    total = total + a * x + b
    print(total)
  return mul_add

c = calc()
c(1)
c(2)


# 호출 횟수를 세는 함수 만들어보기

def counter():
  i = 0
  def count():
    nonlocal i
    i += 1
    return i
  return count


c = counter()
for i in range(10):
  print(c(),end ='')
print()
  
# 최종문제

def countdown(n):
  x = n + 1
  def result():
    nonlocal x
    x -= 1
    return x
  return result
  
  
n = int(input())
c = countdown(n)

for i in range(n):
  print(c(),end=' ')