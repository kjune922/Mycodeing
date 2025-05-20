# 튜플에서 특정 값의 인덱스 구하기
a = (38,21,53,62,19,53)
a.index(53)
print(a.index(53))

# 갯수 구하기
print(a.count(53)) # 53이라는 요소가 몇개있냐?

for i in a:
  print(i,end=' ')


b = (1.2, 2.5, 3.7, 4.6)
b = tuple(map(int,b))
print(b)  
print(min(a))
print(max(a))
print(sum(a))

a,b = map(int,input().split())

x = [i for i in range(a,b+1)]
for i in range(len(x)):
  x[i] = 2**x[i]
x.remove(x[1])
del x[-2:-1]
print(x)