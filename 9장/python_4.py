# Unit 9. 문자열 사용하기

hello = 'Hello, world!'
print(hello) # 결과 Hello world!

hello_2 = "안녕하세요"
print(hello_2) # 한글도 가능 그리고 작은따옴표나, 큰따옴표는 같음 2개든 3개든간에에

hello_3 = '''Hello, world!'''
print(hello_3)

python = """Python Programing"""
print(python)

# 여러 줄 출력해보기
# 작은 따옴표나 큰 따옴표 3개로 시작함

hello_4 = '''Hello, world!
안녕하세요
Python 입니다'''
print(hello_4)

# 문자열 안에 작은따옴표나 큰따옴표 포함하기

# 문자열안에 작음따옴표를 넣고싶다 >> 그럼 문자열을 큰 따옴표로 묶어준다

s = "Python isn't difficult"
print(s)

# 그 반대도 가능

s_1 = 'He said "Python is easy"'
print(s_1)

# 하지만 작음따옴표안에 작은, 큰따옴표안에 큰 따옴표는 불가능
# 근데 여러줄로 된 문자열은 가능 

single_quote = '''"안녕하세요."
'파이썬입니다.'''

double_quote1 = """"HEllo"
'Python'"""

double_quote2 = """Hello, 'Python'""" # 한줄짜리

print(single_quote)
print(double_quote1)
print(double_quote2)

# 참고용 문자열안에 따옴표를 포함하는 다른방법

a = 'Python isn\'t difficult'
print(a)

# 따옴표 세 개로 묶지 않고 여러 줄 입출력 해보기

print('Hello\nPython')

# 사실 따옴표 3개할때 엔터쳐지는 부분마다 \n 이 들어가있음

b =('''Hello
Python''')

c = '''\'Python\' is a \"programming language\" 
that lets you work quickly
and
integrate systems more effectively.'''
print(c)