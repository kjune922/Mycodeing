# Unit 30. 위치 인수와 리스트 언패킹 사용하기

# 지금까지는 간단하게 'Hello, world!' 를 출력하는 함수와 두 수를 더하는 것만 만듬
# 파이썬에서는 함수를 좀 더 편리하게 사용할 수 있도록 다양한 기능 제공
# 함수에서 위치인수, 키워드 인수를 사용하는 방법과 리스트, 딕셔너리 언패킹(unpacking)을 활용하는 방법을 알아보자

# 다음과 같이 함수에 인수를 순서대로 넣는 방식을 위치 인수(positional argument)라고 한다.
# 즉, 인수의 위치가 정해져있다 

print(10,20,30)

# 위치 인수를 사용하는 함수를 만들고 호출하기
# 숫자 세개를 각 줄에 출력하는 함수 만들기

def print_numbers(a,b,c):
  print(a)
  print(b)
  print(c)
  
print_numbers(10,20,30)

# 언패킹 사용하기

# 이렇게 인수를 순서대로 넣을 때는 리스트나 튜플을 사용할 수 도 있다.
# 다음과 같이 리스트 또는 튜플 앞에 *(애스터리스크)를 붙여서 함수에 넣어주면 됨

x = [10,20,30]
print_numbers(*x)

# print_numbers에 10,20,30 이 들어있는 리스트 x를 넣고 *만 붙였는데도 숫자가 각 줄 출력됨
# 즉 , 리스트나 튜플앞에 *를 붙이면 언패킹(unpacking)되서 print_numbers(10,20,30)하고 똑같이 동작이 됨
# 말 그대로 리스트의 포장을 언박싱한다고 이해 ㄱㄱ

# 단, 이때 함수 매개변수 갯수랑 리스트의 요소 갯수가 같아야함

# 가변 인수 함수 만들기
# 인수의 갯수가 정해지지않은 언제든지 변할 수 있는, 가변 인수(variable argument)에 사용한다.
# 즉, 같은 함수에 한개도 가능하고 10개도 가능, 또는 안넣을 수도있음

# def 함수이름(*매개변수)
#     코드


def print_numbers(*args):
  for arg in args:
    print(arg)
    
print_numbers(10) # 1개도 ㄱㄴ
print_numbers(10,20,30,40,50) # 5개도 ㄱㄴ

print_numbers(*[10,20,30,40])
y = ['h','e','l','l','o']
print_numbers(y)
print_numbers(*y)

# 키워드 인수 사용하기

# 지금까지 함수에 인수를 넣을 때 값이나 변수를 그대로 넣었음
# 이제 각각의 용도에 맞기 구별해서 넣을거임

def personal_info(name,age,address):
  print("이름: ",name)
  print("나이: ",age)
  print("주소: ",address)

# 애는 매개변수와 인수가 서로 순서가 맞아야함
personal_info("홍길동", 30, "서울시 용산구 이촌동")

# 명시적인 방법, 이건 순서알빠노임 
personal_info(name="이경준", age=27, address="수영구 민락동")



# 지금까지는 함수를 호출할 때 키워드 인수로 직접 값을 넣음
# 이번에는 딕셔너리를 사용해서 키워드 인수로 값을 넣는 딕셔너리 언패킹할거임
# 함수(**딕셔너리) < 애는 애스터리스크 2개씀

def personal_info(name, age, address):
  print("이름: ",name)
  print("나이: ",age)
  print("주소: ",address)

x = {"name": '홍길동',"age": 30, "address": '충남 계룡시'}
personal_info(**x)

# 왜 2번쓰냐, 딕셔너리는 키 - 값 이렇게 안에 2개씩 짞을 지었으니
# *한번에 키, *또 한번에 값 이렇게 할려고 
# 리스트는 그딴거없잖슴 ㅋ

# 키워드 인수를 사용하는 가변 인수 함수 만들기

# def 함수이름 (**매개변수)
#   코드

def personal_info(**kwrags):
  for kw, arg in kwrags.items():
    print(kw, ': ', arg, sep='') # 구조 설계
    
personal_info(name = "이경준")
personal_info(name="이경준",age="27")

personal_info(name = "이경준", age = "27", address = "부산", job = "대학생")

x = {'name' : '이경준'}
personal_info(**x)
y = {"name": '이경민',"age": "25","address":"창원"}
personal_info(**y)

korean, english, mathematics, science = 100, 86, 81, 91
 