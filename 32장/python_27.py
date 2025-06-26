# Unit 32. 람다 표현식 사용하기
# 람다 표현식은 식 형태로 되어 있다고 해서 람다 표현식이라고 부른다.
# 특히 람다표현식은 함수를 간편하게 작성할수있어서 다른 함수의 인수를 넣을 때 주로 사용


def plus_ten(x):
  return x + 10

print(plus_ten(1))

# 저 위에 함수를 람다표현식으로 바꿔보자

plus_ten = lambda x : x + 10
print(plus_ten(1))

# 람다 표현식을 인수로 사용해보기

# 그 전에 먼저 def함수로 map사용해보기

def plus_ten(x):
  return x + 10

print(list(map(plus_ten, [1,2,3])))

# 위 함수를 람다표현식으로 ㄱㄱ
a = list(map(lambda x: x + 10, [4,5,6]))
print(a)

# 람다 표현식에 조건부 표현식 사용해보기

# 다음은 map을 사용해서 리스트 a에서 3의 배수를 문자열로 변환한다
a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x : str(x) if x % 3 == 0 else x, a)))

# 람다 표현식 내에서는 if, else를 사용할때 ":" 을 붙이지 않는다 기억하기
# 그리고 람다에선 if를 썼으면 무조건 else로 끝을 내야한다 
# 그리고 람다에선 elif 사용못함, if쓰고 else쓰고 if쓰고 else쓰고 이렇게 해야함

# ex) 리스트에서 1은 문자열로 변환하고, 2는 실수로 변환, 3 이상은 10을 더하는 식 표현해보기

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x : str(x) if x == 1 else float(x) if x == 2 else x + 10, a)))
# 넘 억지니까 이럴땐 걍 def함수쓰셈 ㅋ

def f(x):
  if x == 1:
    return str(x)
  elif x == 2:
    return float(x)
  else:
    return x + 10
  
print(list(map(f,a)))

# map에 객체를 여러개 넣어보기
# 두 리스트의 요소를 곱해 하나의 새 리스트 만들기
a = [1,2,3,4,5]
b = [2,4,6,8,10]

print(list(map(lambda x, y : x * y, a, b)))

# filter 사용하기

# filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져온다
# filter에 지정한 함수의 반환값이 True일 때만 해당 요소를 가져온다

# filter(함수, 반복가능한 객체)

# def예시
def f(x):
  return x > 5 and x < 10

a = [8,3,2,10,15,7,1,9,0,11]
print(list(filter(f,a)))

print(list(filter(lambda x : x > 5 and x < 10, a)))

# reduce 사용하기

# reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수이다
from functools import reduce

# reduce(함수, 반복가능한 객체)

# 다음은 리스트에 저장된 요소를 순서대로 더한 뒤 누적된 결과를 반환한다

def f(x,y):
  return x  + y

a = [1,2,3,4,5]
print(reduce(f,a)) # 1+2 하고 거기에 +3 거기에 +4 거기에 +5

print(reduce(lambda x,y:x+y,a)) # 파라미터 x,y를 지정

# 이거를 for반복문으로도 표현가능

x = a[0]
for i in range(len(a)-1):
  x = x + a[i + 1]

print(x)

# 이미지 파일만 가져오기
files = ['font','1.png','10.png','11.gif','2.jpg','3.png','table.xslx','spec.docx']
print(list(filter(lambda x : x.find('.jpg') != -1 or x.find('.png') != -1, files)))


files = input().split()

print(list(map(lambda x : f"{int(x.split('.')[0]):03d}.{x.split('.')[1]}",files)))



# f문자열{값}

# 예시

name = "lee"
age = 27
print(f"Hello my name is {name} and my age is {age}years old")

# 문자열 포매팅

# inf(x.split('.')[0]):03d -> 문자열을 정수로 필수로 바꿔주고, 그리고 "."으로 1.png를 1 = 0번째 인덱스, png = 1번째 인덱스로 나눈다
# 그리고 괄호닫고 03d를 하는건 0은 빈자리를 0으로 채운다, 3은 총 3자리이다, d는 정수 형식으로 출력하겠다 라는 뜻이다