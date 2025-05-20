# 리스트에 map 사용해보기
# 실수가 저장된 리스트가 있을 때, 이 리스트의 모든 요소들을 정수로 변환하려면?

# 방법 1
a = [1.2, 2.5, 3.7, 4.6]
print(a)
for i in range(len(a)):
  a[i] = int(a[i])
print(a)

# 방법 2
a = [1.2, 2.5, 3.7, 4.6]
print(a)
a = list(map(int,a))
print(a)

b = list(map(str,range(5)))
print(b)

a = map(int,input().split())
print(a)
print(list(a))
a, b = [10,20]
print(a)
print(b)

# map(int,input().split()) 을 파헤쳐보자
x = input().split() # 이 결과는 문자열 리스트
m = map(int,x) # 리스트의 요소를 int로 변환, 결과는 맵 객체
a,b = m # 맵 객체는 변수 여러 개에 저장할 수 있음 여기서 a,b변수가 2개니까 2개 입력해줘야함 딱맞게
print(a)
print(b)

