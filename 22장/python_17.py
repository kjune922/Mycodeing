# Unit 22. 리스트와 튜플 응용하기

# 리스트에 요소 추가하기
# append : 요소 하나를 추가
# extend : 리스트를 연결하여 확장
# insert : 특정 인덱스에 요소 추가

a = [10,20,30]
a.append(500)
print(a)
print(len(a))

a = []
a.append(10)
print(a)

# 리스트안에 리스트 추가하기
# append는 append(리스트)처럼 리스트를 넣으면 리스트안에 리스트가 들어간다
# 중첩리스트 예시

a = [10,20,30]
print(a)
print(len(a))
a.append([500,600])
print(a)
# [500,600]을 하나의 요소로봐서 길이가 1밖에안늘어남
print(len(a))

# 즉, append로 추가하면 항상 길이가 1씩 늘어난다

# 리스트 확장하기 >> 리스트에 여러 요소 추가하는 방법
# extend(리스트) 사용

a = [10,20,30]
a.extend([500,600])
print(a)
print(len(a))

# 리스트의 특정 인덱스에 요소 추가하기
# 원하는 특정위치에 요소를 추가하는 방법
# insert(인덱스, 요소) 사용

a = [10,20,30]
a.insert(2,500)
print(a)
print(len(a))

# insert꿀팁
# insert(0, 요소) >> 리스트의 맨처음에 요소추가
# insert(len(리스트명),요소) >> 리스트의 맨끝에 요소추가 # append랑 비슷한데 append는 무조건끝에들어가고, insert는 암때나 가능

# 슬라이스 활용

a = [10,20,30]
a[1:1] = [500,600] # 1번째 인덱스에 500,600을 추가
print(a)

# 리스트에서 요소 삭제하기
# pop : 마지막 요소 또는 특정 인덱스의 요소를 삭제
# remove : 특정 값을 찾아서 삭제

a = [10,20,30]
print(a.pop())
print(a)

# 여기서 pop을 활용해서 원하는 인덱스만 따로 삭제하는 방법
# pop(인덱스 몇번째?) 활용

a = [10,20,30]
a.pop(1)
print(a)

# 사실 pop 대신 del 사용해도 알빠노

# 특정 값 찾아서 삭제하는 remove

a = [10,20,30]
a.remove(20)
print(a)

a = [10,20,30,20]
a.remove(20) # 만약 이렇게 리스트내에 동일한 값이 2개있으면 앞에것부터 삭제
print(a)


