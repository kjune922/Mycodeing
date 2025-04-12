# 출력 방법 알아보기
import sys
# 파이썬 행렬계산
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])  # 3x3 행렬 생성
b = np.array([[1,2,3],[4,5,6],[7,8,9]])  # 3x3 행렬 생성
print(a@b) # 행렬곱셈


# 1. 값을 여러 개 출력

print(1,2,3)
print('hello','python')

# 2. sep로 값 사이에 문자넣기
print(1,2,3,sep=',')
print(1920,1080, sep = 'x')

# 줄바꿈 활용하기 
print(1,2,3,sep ='\n')

# 이것도 가능
print('1\n2\n3')

# print는 기본적으로 끝에 '\'을 붙힌다
print(1)
print(2)
print(3)

# print로 문자들을 나열해서 출력
print(1,end='')
print(2,end='')
print(3)

# end=''와 같이 end에 빈 문자열을 지정하면 1,2,3이 세줄로 출력되지않고 한 줄로 출력됨, 왜냐하면 print의 end가 끝에 기본적으로 있던
# \n을 지워버리고 ''으로 대신하기떄문

print(1,end=' ')
print(2,end=' ')
print(3)

print('Hello','Python',end='\n')
print('Hello','Python',sep='\n')

year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year,month,day,sep='/',end=' ')
print(hour,minute,second,sep=':')

year,month,day,hour,minute,second = input().split()
print(year,month,day,sep='-',end='T')
print(hour,minute,second,sep=':')

print(sys.getrefcount(year))