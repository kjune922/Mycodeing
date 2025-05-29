# Unit 26. 세트 사용하기
# 파이썬은 집합을 표현하는 세트(set)라는 자료형을 제공한다
# 집합을 영어로 하면 세트인데, 수학에서 배우는 그 집합이 맞다 ㅋ
# 따라서 합집합, 교집합, 차집합 등의 연산이 가능

# 세트 만들어보기

fruits = {'strawberry','grape','orange','pineapple','cherry'}
print(fruits)

# 세트는 단순히 집합을 의미하지 순서를 의미하지않기에 매번 출력이 지 ㅈ대로 나온다
# 또 요소의 중복은 불가능하다 중복해도 한개만 출력한다

# print(fruits[0]) 집합은 이렇게 출력 불가능하다

# 세트에 특정값이 있는지 확인하려면??
print('orange'in fruits)
print('peach'in fruits)

# 반대로 in앞에 not을 붙이면 없는지 확인함
print('orange'not in fruits)
print('peach'not in fruits)

# set를 이용해서 만들어보기
# set(반복가능한 개체)
a = set('apple')
print(a)

# 0부터 4까지 집합
b = set(range(5))
print(b)

# 빈 세트
c = set()
print(c)

# 프로즌세트 :: 얼린세트 (변경불가) const느낌

a = frozenset(range(10))
print(a)

# 프로즌세트는 프로즌세트안에 프로즌세트를 넣을 수 있다. 근데 세트는 안받아줌 
b = frozenset({frozenset({1,2,3}),frozenset({4,5,6})})
print(b)

# 집합 연산 사용해보기
# 집합 연산은 파이썬의 산술 연산자와 논리 연산자를 활용한다
# "|" 연산자는 합집합을 구하며 OR연산자중 작대기 한개만쓴다
# set.union하고 똑같음

a = {1,2,3,4}
b = {3,4,5,6}
print(a | b)
print(set.union(a,b))

# & 연산자는 교집합(intersection)을 의미한다, AND연산자인 &&에서 한개만 떼어왔다
# set.intersection 하고 똑같음

print(a & b)
print(set.intersection(a,b))

# - 연산자는 차집합(difference)을 구하며 뺄셈 연산자 "-"을 사용한다
# set.difference 메서드하고 동작이 똑같음

print(a - b)
print(set.difference(a,b))

# "^" 연산자는 대칭차집합(symmetric difference)을 구하며 XOR연산자 ^ 을 사용한거임
# set.symmetric_difference 하고 동작이 같음
# XOR은 서로다르면 "참이다", 그래서 결과로 겹치지않는 요소만 출력한다

print(a^b)
print(set.symmetric_difference(a,b))

# 집합연산 후 할당 연산자 사용하기
# 세트1 | = 세트2 >> 세트1.update(세트2)

a = {1,2,3,4}
a |= {5}

print(a)

a.update({6})
print(a)

# &= 현재 세트와 다른 세트중 겹치는 요소만 현재 세트에 저장하며
# 세트1.intersection_update(세트2) 하고 같다

a = {1,2,3,4}
a &= {0,1,2,3,4}
print(a)
a.intersection_update({2,3})
print(a)

# -= 은 현재 세트에서 다른 세트를 빼며 difference_update 메서드와 같다
a = {1,2,3,4}
a -= {3}
print(a)
a.difference_update({2,4})
print(a)

# ^= 은 현재 세트와 다른 세트 중에서 겹치지 않는 요소만 현재 세트에 저장
# symmetric_difference 메서드랑 같음

a = {1,2,3,4}
a ^= {3,4,5,6}
print(a)
a.symmetric_difference_update({5,6,7,8})
print(a)

# 부분집합과 상위집합 확인하기

# <= 은 현재 세트가 다른 세트의 부분집합(subset)인지 확인하며 issubset메서드와 같다
a = {1,2,3,4}
print(a <= {1,2,3,4,5})
print(a <= {1,2,3,4,5,6})
print(a.issubset({1,2,3}))

# < 은 현재 세트가 다른 세트의 진부분집합(proper subset)인지 확인하며 메서드는 없습니다.
# 다음은 세트{1,2,3,4}가 세트 {1,2,3,4,5}의 진부분집합이므로 참이다.
# 즉, 부분집합이지만 같지는 않을 때 참이다

a = {1,2,3,4}
print(a<{1,2,3,4})
print(a<{1,2,3,4,5})

# >= 은 현재 세트가 다른 세트의 상위집합(superset)인지 확인하며 issuperset 메서드와 같다.
# 다음은 세트 {1,2,3,4}가 {1,2,3,4}의 상위집합이므로 참이다
# 등호가 이렇게 있으면 두 세트가 같을 때도 참이다
a = {1,2,3,4}
print(a>={1,2,3,4})
print(a.issuperset({1,2,3,4,5}))
print(a.issuperset({1,2}))

# >은 현재 세트가 다른 세트의 진상위집합인지 확인

a = {1,2,3,4}
print(a>{1,2,3,4})
print(a>{1,2,3})

# 세트는 "=="사용가능
# "!="도 사용가능 

# 세트가 겹치진 않는지 확인해보기
a = {1,2,3,4}
print(a.isdisjoint({5,6,7,8})) # 겹치는 요소없음
print(a.isdisjoint({1,2,3}))

# 이번에는 세트에 요소를 추가해보자
# 세트.add(요소)

a = {1,2,3,4}
a.add(5)
print(a)

# 세트에서 특정 요소 삭제해보기
a.remove(5)
print(a)

# remove는 삭제할요소가 없으면 에러발생
# 근데 discard(요소)는 없으면 유도리있게 넘어감
a.add(5)
a.discard(5)
a.discard(6)
print(a)
a.discard(2)
print(a)

# 세트에서 pop()은 임의로 랜덤으로 아무거나 하나삭제시킴
a = {1,2,3,4}
print(a.pop()) # 그리고 반환함
print(a)

# 세트의 모든 요소 삭제는
a.clear()
print(a)

# 세트의 요소 갯수구하기
a = {1,2,3,4}
print(len(a))

# 할당하는거
a = {1,2,3,4}
b = a 
a.add(5)
print(a)
print(b)
# 아직 세트는 1개다
a = {1,2,3,4}
b = a.copy()
a.add(5)
print(a)
print(b)
# 이럼 2개다다