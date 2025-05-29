# 세트와 for반복문을 사용해서 요소 출력해보기
# for 변수 in 세트:
#   반복할 코드

a = {1,2,3,4}
for i in a:
  print(i)
  
# 세트 컴프리핸션

a = {i for i in 'apple'} # 첫번째 i로 세트 생성, 두번쨰 i로 문자열 'apple'에서 한개씩 꺼내서 두번째 i에 넣는다
print(a) # 중복되는 p는 하나만쓴다

a = {i for i in 'pineapple' if i not in 'apl'} # "a","p","l" 를 제외하고 문자들을 세트로 생성
print(a) # 이와중에 e는 중복되서 한개만출력

# 값은 is, is not으로 컴프리핸션에 비교하면안됨
# ex) {i for i in range(10) if i is not 2 and i is not 7} 안됨

a,b = map(int,input().split())
a = {i for i in range(1,a+1) if a % i == 0}
b = {i for i in range(1,b+1) if b % i == 0}

divisor = a&b # 교집합
result = 0
if type(divisor) == set:
  result = sum(divisor)
  
print(result)