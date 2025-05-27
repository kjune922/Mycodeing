# Unit 24. 문자열 응용하기

# 문자열 바꾸기, replace("바꿀 문자열", "새 문자열") 은 왼쪽문자열을 오른쪽 문자열로 바꾼다

a = "Hello, world!"
print(a)
print("Hello, world!".replace("world!","LEE!"))
a = a.replace("world!","python!")
print(a)

# replace는 문자열을 바꾸고
# translate는 문자열 안의 문자를 다른 문자로 바꾼다.
# 먼저 str.maketrans("바꿀문자", "새문자") 로 변환 테이블을 만든다.
# 그 다음에 translate(테이블)을 사용하면 문자를 바꾼 뒤 결과를 반환한다.

table = str.maketrans("aeiou",'12345')
print("apple".translate(table))

# 문자열 분리해보기
# split()은 공백을 기준으로 문자열을 분리하여 리스트로 만든다. 지금까지 input으로 입력받은 문쟈열을 리스트로 반환하는게 이 split()이놈이다

print("apple pear grape pineapple orange".split())
print("apple, pear, grape, pineapple, orange".split(","))

# 구분자 문자열과 문자열 리스트 연결하기
# 문자열을 split()으로 서로 구분했으니 이젠 연결해보자
# join(리스트)는 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만든다.

print('여기에뭘넣든 이걸로 구분함'.join(['apple','pear','grape','pineapple','orange']))
print('-'.join(['apple','pear','grape','pineapple','orange']))

# 소문자를 대문자로 바꾸기
# upper()는 문자열과 문자를 모두 대문자로 바꾼다

print('python'.upper())

# 대문자를 소문자로 바꾸기
# lower()는 문자열의 문자를 모두 소문자로 바꾼다

print('PYTHON'.lower())

# 왼쪽 공백 삭제하기
# 문자열을 사용하다 보면 공백을 삭제해야할 때가 있다, 이때 lstrip, rstrip, strip 메서드를 사용한다
# lstrip()은 왼쪽에 있는 연속된 모든 공백 삭제

print('    Python'.lstrip())

# rstrip()은 오른족에 있는 연속된 모든 공백 삭제

print('Python    '.rstrip())

# 양쪽 공백 다 삭제하기

# strip()은 양쪽 다 지워버림

print('    Python     '.strip())

# 왼쪽의 특정 문자 삭제하기
print(',Python.'.lstrip(',.'))

# 오른쪽 특정 문자 삭제하기
print(',Python.'.rstrip(',.'))

# 양쪽 특정 문자 삭제하게
print(',Python.'.strip(',.'))

# 문자열을 왼쪽 정렬하기

print('python'.ljust(10))

# 문자열을 오른쪽 정렬하기
print('python'.rjust(10))

# 문자열 가운데 정렬하기
print('python'.center(10))

# 정렬하기에서 (이만큼 총 길이)를 정해서 왼쪽으로 붙이고 오른쪽으로 붙이고 중앙에 정렬한다

# 문자열 가운데 정렬하기인데 총길이가 홀수
print('python'.center(11)) # 남는 공백을 왼쪽에 붙임 3칸 python 2칸 이렇게

## 중요
# 쉼표나 콤마, 느낌표같은것들 삭제하는 방법

import string

x = 'python.,!@#!#!#@'.strip(string.punctuation)
print(x)

print(string.punctuation)