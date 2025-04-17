# Unit 11. 시퀀스 자료형 활용하기

# 파이썬에서는 리스트, 튜플, range, 문자열처럼 값이 연속적으로 이어진 자료형을 시퀀스 자료형(sequence types)라 한다
# ex)list, tuple, range, str, bytes, bytearray

# 시퀀스 자료형의 공통 기능 사용하기 !

# 시퀀스 자료형으로 만든 객체를 시퀀스 객체라고 하며, 시퀀스 객체에 들어있는 각 값을 요소라고 부릅니다

a = [0,10,20,30,40,50,60,70,80,90]
print(30 in a) # 30은 리스트 객체안에있음
print(100 in a) # 100은 없음

# 반대로 in 앞에 not을 붙이면 결과가 반대로나옴

print(30 not in a)
print(100 not in a)

# 튜플과 range, 문자열도 같은 방법으로 활용가능

print(43 in (38,76,43,62,19))
print(1 in range(10))
print('P'in'Hello,Python')

# 시퀀스 객체 연결하기

a1 = [0,10,20,30]
b = [9,8,7,6]
print(a1 + b)

# 다만 range는 연결이 불가능 >> range + range 는 오류난다
# 이럴때는 range를 리스트나, 튜플로 만들면 연결 가능

print('Hello,' + 'World!')

# 시퀀스 객체 반복하기
c = [0,10,20,30]*3
print(c)

# 마찬가지로 range는 이게안된다 그래서 리스트나 튜플로 바꿔서 ㄱㄱ

print(list(range(0,5,2))*3)
print(tuple(range(0,5,2))*3)

# 문자열도 가능

print('Hello!'*3)

