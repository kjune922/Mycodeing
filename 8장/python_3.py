# Unit 8. 불과 비교, 논리 연산자 알아보기
# 참, 거짓을 나타내는 boolean


print(True)
print(3>2)
print(10==10)
print(10 != 5)
print(10 is not 5)
print(10 is 10)

# 실수 1.0 하고 정수 1은 다르다 서로
print(1 is not 1.0)

# 논리 연산자 써보기
print(True and True)
print(True and False)

print(True or False)
print(True or True)

# not 은 논리값을 뒤집는다
print(not True and False or not False)

# 괄호로 표시한 것, 이렇게 순서가 헷갈릴때는 괄호로 표시해주는 것이 좋다
print((not True)and False or (not False))

# 파이썬에서 비교 연산자 순서 >> (is , is not , == , != , < , > , <= , >=)

# 정수, 실수, 문자열을 bool로 만들기
# 0, 0.0, 빈 문자열 제외 모두 True
bool(1)
bool(0) # 이건 False를 의미
bool(1.5)
bool('False')

## 단락평가
# 단락 평가란 첫 번째 값으로 (and 제외) 결과가 확실할때 두번째는 평가하지않는것

print(True and False)
print(False and True)

# 그리고 단락 평가를 마지막에 실시해야 bool값을 내보냄
print(True and 'Python') # Python 출력
print('Python' and True) # True 출력

a = 10; b = 20
print(not b != 20 and a > 5)

korean, english, mathmatics, science = input().split(' ')
print(int(korean) >= 90 and int(english) > 80 and int(mathmatics) > 85 and int(science) >= 80)