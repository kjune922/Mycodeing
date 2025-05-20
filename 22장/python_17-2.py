# 리스트로 스택과 큐 만들어보기

# from collections import deque >> collections 모듈에서 deque를 가져온다는 뜻
# deque의 append는 덱의 오른쪽에 요소 추가
# deque의 popleft는 덱의 왼쪽요소 삭제
# deque의 appendleft는 왼쪽에 요소 추가
# deque의 pop으로 덱의 오른쪽 요소 삭제

from collections import deque

a = deque([10,20,30])
print(a)
a.append(500)
print(a)
a.popleft()
print(a)
a.appendleft(400)
print(a)
a.pop()
print(a)

# 스택은 새로운놈이 들어오면 들어오는 위치에있던 원래친구가 빠져나감
# 큐는 새로운놈이 들어오면 맨뒤에있는애가 날라감

# 리스트에서 특정 값의 인덱스 구하기
# index(값)은 리스트에서 특정 값의 인덱스를 구함 (인덱스 >> 순서) , 그리고 동일한 요소가 있으면 앞에 꺼부터!
a = [10,20,30,15,20,40]
print(a.index(20))

#  특정 값의 개수 구하기
# count(값)은 리스트에서 특정 값의 개수를 구한다
a = [10,20,30,15,20,40] # 20이 2개있음
print(a.count(20)) # 2

# 리스트의 순서 뒤집기
# reverse()는 리스트에서 요소의 순서를 반대로 뒤집는다.
a = [10,20,30,15,20,40]
print(a)
a.reverse()
print(a)

# 리스트의 요소 정렬하기
# sort()는 리스트의 요소를 작은 순서대로 정렬한다 (오름차순)
# sort(reverse=False) : 리스트를 오름차순 정리
# sort(reverse=True) : 리스트를 내림차순 정리
a = [10,20,30,15,20,40]
a.sort(reverse=False)
print(a) # 내림차순
a.sort(reverse=True)
print(a) # 오름차순 

# sort(), sorted()
a = [10,20,15,30,20,40]
a.sort()
print(a) # a를 바꿈

b = [10,20,15,30,20,40]
sorted(b)
print(b)
print(sorted(b)) # 새 리스트 생성

# sort는 a를 바꾸고, sorted()는 아예 새 리스트자체를 생성

# 리스트의 모든 요소 삭제해보기
# clear()는 리스트의 모든 요소를 삭제한다.
a = [10,20,30]
a.clear()
print(a)

# del 사용가능
a = [10,20,30]
del a[:]
print(a)

# 리스트를 슬라이스로 조작하기
a = [10,20,30]
a[len(a):] = [500] # append(500)하고 같음
print(a) 

# 리스트가 비어있는지 확인해보기!!
seq = [100,200]

if not len(seq): # 리스트가 비어있으면 True
  print("리스트 요소없음")
elif len(seq): # 리스트에 요소가 있으면 True
  print("리스트 요소있음")

print(seq[0])
print(seq[1])
print(seq[-1])