# Unit 22 리스트의 할당과 복사 알아보기

# 할당과 복사는 비슷한거같지만, 큰 차이가 있다
# 먼저 리스트하나를 만들고 다른 변수에 할당한다

a = [0,0,0,0,0]
b = a # 그래도 리스트는 1개다
print(a is b)

# a와 b는 같으므로, b[2] = 99와 같이 리스트 b의 요소를 변경하면 리스트 a와 b에 모두 반영된다
b[2] = 99
print(a)
print(b)

# 리스트 a와 b를 완전히 두 개로 만들려면 copy 매서드로 모든 요소를 복사해야 한다
a = [0,0,0,0,0]
b = a.copy()
print(a is b)
print(a == b)

b[2] = 100 # 이제 a,b 모두반영이 안되고 b에만 반영됨
print(a)
print(b) 

# 반복문으로 리스트의 요소를 모두 출력해보기

a = [38,21,53,62,19]
for i in a:
  print(i)
  
for i in [38,21,53,62,19]:
  print(i)

# 인덱스와 요소를 함께 출력하기

a = [38,21,53,62,19]
for index,value in enumerate(a):
  print(index,value)
  
# 꼴받아서 만약 인덱스 1부터 출력마렵다면?

for index,value in enumerate(a):
  print(index+1,value)
  
# 파이썬같은 방법 > 시건방떨기

for index, value in enumerate(a,start=0):
  print(index,value)
  
for index, value in enumerate(a,0): # 요로코롬 쓸수도있음
  print(index,value)

# 그냥 다 귀찮고 바로 인덱스로 요소 출력하기

for i in range(len(a)):
  print(a[i]) # 요소
  print(i) # 인덱스
  
# while반복문으로 요소 출력하기

i = 0
while i < len(a):
  print(a[i])
  i+=1
  
