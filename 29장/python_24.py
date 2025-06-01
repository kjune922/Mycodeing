# Unit 29. 함수 사용하기

# 파이썬은 함수(Function)라는 기능을 제공하는데, 특정 용도의 코드를 한 곳에 모아 놓은 것을 뜻함
# 그래서 함수는 처음 한번만 작성해놓으면 계속 불러서 쓸수있음

# ex) print, input, 등 도  모두 파이썬에서 미리 만들어 둔 함수임 
# 함수를 사용하면
# 1. 코드의 용도를 구분할 수 있음
# 2. 코드를 재사용할 수 있음
# 3. 실수를 줄일 수 있음

# 함수는 "def"에 함수 이름을 지정하고 "()"와 ":"을 붙인 뒤 다음 줄에 들여쓰기해서 원하는 코드 작성

def hello():
  print('Hello, world!')
  
hello()

# 이제 파이썬 스크립트에서 함수의 실행 순서를 알아보겠습니다.
# 1. 파이썬 스크립트 최초 실행
# 2. hello 함수 호출
# 3. hello 함수 실행
# 4. print함수 실행 및 "Hello, world!" 출력
# 5. hello 함수 종료
# 6. 파이썬 스크립트 종료


# 비어있는 함수 만들기

def hello():
  pass

# 그냥 아무 역할도없이 함수 틀만 유지한다 

# 함수에서 값을 받으려면 "()"안에 변수 이름을 지정해주시면 됩니다.
# 특히 이 변수를 매개변수(parameter)라고 부른다.

# def 함수이름(매개변수1, 매개변수2):
     # 코드
     
def add(a,b):
  print(a+b)
  
add(3,4)

# 파이썬용 주석 "독스트링" ㅈ같긴한데 알아보기

def add(a,b):
  """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수임"""
  print(a + b)
  
add(5,6)
print(add.__doc__) # 애는 함수안에있는 독스트링을 반환

# return 써보기
# 앞에서 만든 add는 두 수를 더해서 바로 출력함
# 그럼 함수에서 값을 꺼내오려면??

# def 함수이름(매개변수):
  # return 반환값


def add(a,b):
  return a+b

x = add(3,5)
print(x)

# 참고로 return을 활용해서 함수중간에 빠져나올수도있음

def not_ten(a):
  if a == 10:
    print("빠져나옴")
    return
  print(a, '입니다',sep='')
  
b = int(input())
not_ten(b)

def add_sub(a,b):
  return a+b,a-b

print(add_sub(10,5))

