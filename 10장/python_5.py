# Unit 10. 리스트와 튜플 사용하기

# 지금까지는 변수에는 값을 한 개씩만 저장했다
a = 10
b = 20

# 중요!! 리스트 만들기

a1 = [38,21,53,62,19]  # 안에있는값은 요소라고 부른다
print(a1)

# 리스트에 여러가지 자료형 저장하기

person = ['janmes',17,175.3,True]
print(person)

# 비어있는 리스트만들기
a2 = []
print(a2)

b1 = list()
print(b1)

# range를 사용해서 리스트 만들기
# range는 연속된 숫자를 생성한다, range(10)은 0부터 9까지 생성

range(10)
print(range(10))

a3 = list(range(10))
print(a3)

# 증가폭을 사용하는 방법 range에 증가폭을 지정하면 해당 값만큼 증가하면서 숫자생성

# 리스트 = list(range(시작, 끝, 증가폭)) 그리고 끝은 포함시키지않음

b2 = list(range(0,10,2))
print(b2)

# 만약 증가폭을 음수로하면 증가폭만큼 숫자들이 감소하면서 내림차순이됨

b3 = list(range(10,0,-1))
print(b3)

## 튜플 사용하기
# 튜플은 리스트처럼 요소를 일렬로 저장하지만, 안에 저장된 요소를 변경, 추가, 삭제 불가능 >> 읽기 전용 리스트

# 튜플 = (값,값,값)
# 튜플 = 값,값,값

a4 = (38,21,53,62,19)
print(a4)
b4 = 38,21,53,62,19
print(b4)

# 요소가 한개인 튜플만들기
a5 = (38,)
b5 = 38,
print(a5,b5,sep='\n')

# range를 써서 튜플 만들기
aa = tuple(range(10))
print(aa)

bb = tuple(range(0,12,2))
print(bb)

# 튜플을 리스트로, 리스트를 튜플로

aa1 = [1,2,3]
print(tuple(aa1))

bb1 = (4,5,6)
print(list(bb1))

# 참고로 input().split()은 리스트를 반환한다 

print(input().split())
x = input().split()
s,d = x
print(s,d)

# 연습문제 1

A = list(range(5,-10,-2))
print(A)

# 심사문제
B = int(input())
print(tuple(range(-10,10,B)))