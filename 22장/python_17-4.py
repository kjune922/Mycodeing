# 리스트에 저장된 값중 가장 작은 수, 가장 큰 수 , 요소의 합계 구해보기

a = [38,21,53,62,19]
smallest = a[0]
for i in a:
  if i < smallest:
    smallest = i
print(smallest)

# 가장 큰 수는 부등호바꾸면됨

largest = a[0]
for i in a:
  if i > largest:
    largest = i
print(largest)

# 제일 간단한 파이썬 min(), max() 함수 사용
print(min(a))
print(max(a))

# 요소의 합계구해보기
a = [10,10,10,10,10]
x = 0
for i in a:
  x += i
  
print(x)

# ㅋㅋ 파이썬에선 합계구해주는 함수 sum() 있음

sum(a)
print(sum(a))

# 리스트 표현식 사용해보기
# 파이썬에선 리스트안에 for반복문하고 if문 사용가능함
# 이걸 우린 "리스트 컴프리핸션" 이라고 부른다
# 이걸 또 우린 리스트 표현식이라고 부르겠다

a = [i for i in range(10)] # 0부터 9까지 숫자를 생성하여 리스트 생성
print(a)

b = list(i for i in range(10))
print(b)

# [식 for 변수 in 리스트] << 이 방식을 많이 씀
a = [i for i in range(10) if i % 2 == 0]
print(a)

# 0~9 숫자 중에서 홀수만 골라서 5씩더한 값을 요소로 가지는 리스트 생성해보기
b = [i+5 for i in range(10) if i % 2 != 0]
print(b)

# for 반복문과 if조건문 여러번 사용해보기
# 2단부터 9단까지 구구단 생성
a = [i * j for i in range(2,10)
           for j in range(1,10)]
print(a)
