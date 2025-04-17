# 리스트와 튜플의 요소 개수 구하기

a = [0,10,20,30,40,50,60,70,80,90]
print(len(a))

b = (0,1,2,3,4)
print(len(b))

print(len(range(0,10,2)))

print(len('Hello, world!'))

# 인덱스 사용해보기

a1 = [38,21,53,62,19]
print(a1[0]) # 리스트의 첫 번째(인덱스0)요소 출력
print(a1[2]) # 리스트의 세 번째(인덱스2)요소 출력
print(a1[4]) # 리스트의 다섯 번째(인덱스4)요소 출력

b1 = (38,21,53,62,19)
print(b1[0])

r = range(0,10,2)
print(r[2])

hello = 'Hello, world!'
print(hello[7])

## __getitem__메서드

aa = [11,22,33,44]
print(aa.__getitem__(1))

# 음수 인덱스 지정하기

a2 = [38,21,53,62,19]
print(a2[-1]) # 리스트의 뒤에서 첫번째
print(a2[-4]) # 리스트의 뒤에서 4번째

# 튜플, range, 문자열도 음수 인덱스지정하면 뒤에서부터 요소에 접근한다

b2 = (38,21,53,62,19)
print(b2[0])
print(b2[-1])

r1 = range(0,10,2)
print(r1[-3])

print(hello[-4])

# 만약에 인덱스 범위를 벗어난다면?? >> 인덱스에러가 뜸

# 마지막요소 출력 len응용

A = [38,21,53,62,19]
print(A[len(A)-1])

# 요소에 값 할당하기

ar = [0,0,0,0,0]

ar[0] = 1
ar[1] = 2
ar[2] = 3
ar[3] = 4
ar[4] = 5

print(ar)

# 단, 튜플과 range, 문자열은 저장된 요소를 변경 불가능! 애넨 읽기전용임

# del로 요소 삭제도해보자

del ar[1]
del ar[2]
print(ar)

