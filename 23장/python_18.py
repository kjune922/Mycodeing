# Unit 23. 2차원 리스트 사용하기

# 이번에는 평면 구조의 2차원 리스트를 사용해보자
# 가로 x 세로로 이루어져있고, 행과 열 둘다 0부터시작

# 2차원 리스트는 리스트 안에 리스트를 넣어서 만들 수 있으며, 안쪽의 각 리스트는 ,(콤마)로 구분한다

# 리스트 = [[값, 값],[값, 값],[값, 값]]

a = [[10, 20],[30, 40],[50, 60]]

print(a) # 이렇게하면 한줄로되는데 가로 2, 세로 3을 확실하게 보는 방법
a = [[10, 20],
     [30, 40],
     [50, 60]] # 가로 2, 세로 3
print(a)

# 2차원 리스트의 요소 접근해보기
# a[0] [0] >> 세로 인덱스 0, 가로 인덱스 0

print(a[1][1]) # 세로 인덱스 1, 가로 인덱스 1 >> 40
print(a[2][0]) # 세로 인덱스 2, 가로 인덱스 0 >> 50
print(a[2][1]) # 세로 인덱스 2, 가로 인덱스 1 >> 60

# 2차원 리스트에 값 할당

a[0][1] = 1000
print(a[0][1]) # >> 20이 1000이 됐다
print(a)

# 톱니형 리스트 >> (행의 요소 갯수)가 제각각
a = [[10, 20],
     [500,600,700],
     [9],
     [30,40],
     [8],
     [800,900,1000]]
print(a)
# 직접 만들기도 가능
a = []
a.append([])
a[0].append(10)
a[0].append(20)
a.append([])
a[1].append(100)
a[1].append(200)
a[1].append(300)
print(a)

# 만약 2차원 리스트의 출력구조를 사각형으로 하고싶다?? print말고 pprint 사용
from pprint import pprint

a = [[10,20],[30,40],[50,60]]
pprint(a, indent=4,width=20)# indent는 들여쓰기 칸수, # width는 가로 폭
pprint(a, indent=2,width=20)

# for 반복문을 한번만 사용해서 2차원 리스트 만들기

a = [[10,20],[30,40],[50,60]]
for x,y in a: # 리스트의 가로 한 줄(안쪽 리스트)에서 요소 두 개를 꺼낸다
  print(x,y)
  
# for 반복문을 2번 사용해보기

for i in a: # a에서 안쪽 리스트를 꺼냄
     for j in i: # 안쪽 리스트에서 요소를 하나씩 꺼냄
          print(j,end=' ')
     print()

# for와 range 사용하기

a = [[10,20], [30,40],[50,60]]

for i in range(len(a)): # 세로크기
     for j in range(len(a[i])): # 가로크기
          print(a[i][j],end=' ') # 리스트[세로인덱스][가로인덱스] 로 접근한다 요소에
     print() # 엔터키담당
     
# while반복문 한번 사용

i = 0
while i < len(a): # 반복할 때 리스트의 세로크기 활용
     x,y = a[i] # 요소 한방에 가져오기
     print(x,y)
     i+=1

# while반복문 2번 사용

i = 0
while i < len(a):
     j=0
     while j < len(a[i]):
          print(a[i][j],end=' ')
          j+=1 # 가로 1증가해서 while문 탈출
     i+=1 # 세로 1씩 증가
     print() # 엔터키 담당

# for 반복문으로 1차원 리스트 만들어보기

a = []
for i in range(10):
     a.append(0)
print(a)

# for 반복문으로 2차원 리스트 만들어보기

a = [] # 세로인덱스를 담당하는 리스트
for i in range(3):
     line = [] # 가로인덱스를 담당하는 리스트
     for j in range(2):
          line.append([1])
     a.append(line)

print(a)

# 리스트 컴프리핸션으로 2차원리스트 만들어보기

a = [[0 for j in range(2)] for i in range(3)]
     
print(a)

a = [[1 for j in range(4)] for i in range(10)]
print(a)

a = [[1]*2 for i in range(3)]
print(a)

# 톱니형 리스트 만들기
a = [3,1,3,2,5] # 가로 크기를 저장한 리스트
b = [] # 빈 리스트 생성

for i in a: # 가로 크기를 저장한 리스트로 반복
     line = [] # 안쪽 리스스트로 사용할 빈 리스트 생성
     for j in range(i): # 리스트 a에 저장된 가로 크기만큼 안쪽리스트요소 생성
          line.append(0) # 안쪽리스트요소를 0으로해서 추가
     b.append(line) # 이제 안쪽리스트자체를 큰 틀의 리스트 b에 요소로써 추가
print(b)

# sorted로 2차원 리스트 정렬해보기

# 2차원 리스트 정렬할때는 sort가아니고 sorted를 쓴다

students = [
     ['john','C',19],
     ['maria','A',25],
     ['andrew','B',7]
]

print(sorted(students,key=lambda student: student[1])) # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students,key=lambda student: student[2])) # 안쪽 리스트의 인덱스 2를 기준으로 정렬

# 2차원 리스트의 할당과 복사

# 할당 >> 리스트는 1개임
a = [[10,20],[30,40]]
b = a
b[0][0] = 500
print(a)
print(b)

# 복사 >> 리스트가 2개임
a = [[10,20],[30,40]]
import copy
b = copy.deepcopy(a) # 시2발 파이썬 미쳤냐? 2차원이상의 다차원리스트는 copy메서드말고 import copy하고 copy.deepcopy(복사할 리스트) 이지랄해야댐
b[0][0] = 500
print(a)
print(b)

a = [[10,20],[30,40]]
for i in a:
     for j in i:
          print(j)
          
