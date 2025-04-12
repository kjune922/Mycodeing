print('Hello, world!') # 가장 기본적인 print함수

print(1+1) # 사칙연산

print(4/2) # " / "한개는 완전히 나누어 떨어져도 실수반환
print(5.5//2) # 실수는 나오지만 소수점이하는 버림
print(2**10) # 파이썬의 거듭제곱

# 앞에 int가 붙으면 뭐든지 정수형으로 출력해버림
print(int(3.3)) # 숫자
print(int(5/2)) # 계산식 
print(int('10')) # 문자열

# type()은 괄호안에 타입을 알려주는 함수
print(type(10))

# divmod 5를 2로 나누었을때 몫은 2, 나머지는 1이라고 나옴
divmod(5,2)

# 실수와 정수를 함께 계산하면?? >> 실수로나온다 범위가 넓은 실수로 계산된다 float > int

# 값을 실수로 만들기
print(float(5))
print(float(5+3))

# float 클래스 반환
type(3.5)

# complex 복소수
print(complex(1.2,1.3))

# 연산우선순위는 우리가 기존에 배운 수학과 같음
print((35+1)*2)

# 변수만들기
a = 10
# x에 10이라는 정수를 할당
type(a)

x,y,z = 10,20,30

x,y = 10,20
x,y = y,x
# 이러면 x와 y값이 서로바뀜

# 변수삭제
del x
del y
del z

# Null 만들기
x = None

# 변수계산
a = 10
b = 20
c = a + b

# 아래 두 표현은 같다
a = a + 10
a += 10

# 그 외 여러가지 응용용
a *= 10
a /= 10
a -= 10
a **= 10

# input 함수는 사용자가 입력한 값을 가져오는 함수
input()

# input받은 값을 x에 할당
x = input()

# x에 있는값은 내가 입력한 문자열

# cout처럼 쓸수도있음
y = input('문자열을 입력하세요: ')

a = input()
type(a)
# 이러면 결과가 <class 'str'>로 나온다 왜냐 입력받은걸 input함수는 문자열로 반환하기때문에

# 그래서 우리가 int형으로 하고싶으면
a = int(input('첫번째 숫자 입력하세요: '))
b = int(input('두번째 숫자 입력하세요: '))
print(a + b)
# 이러면 결과가 a랑 b를 나열한게 아닌 a + b값이 나옴

# split()을 쓰면 여러번 받을 수있다
aa,bb = input('문자열 두 개를 입력하세요: ').split() # 입력받은 값을 공백으로 구분

# 만약 콤마로 구분하고싶다?
cc,dd = input('문자열 두개를 입력하세여: ').split(",") # 이런식으로 ! 

a,b,c,d = map(int,input().split()) 
print((a+b+c+d)//4)