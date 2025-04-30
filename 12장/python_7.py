# 딕셔너리 만들어보기

# 일반적인 리스트
lux = [490,334,550,18.72]

# 딕셔너리 중괄호로 바꾸면서 ''랑 :가 추가되었다
lux = {'health': 490,'mana': 334,'melee': 550,'armor': 18.72}
print(lux)

# 여기서 health: 와 같은것은 "키"라고 부르고 490은 "키의 값"이라고한다
# 만약 키 이름이 중복된다면 맨오른쪽에 있는 값을 출력한다

# 빈 딕셔너리 만들기
x = {}
print(x)
y = dict()
print(y)

# dict함수로 딕셔너리 만들어기 
# 1. 딕셔너리 = dict(키 = 값1, 키2 = 값2)
# 2. 딕셔너리 = dict(zip(['키1', '키2'], [값1, 값2]))
# 3. 딕셔너리 = dict([('키1', 값1),('키2', 값2)])
# 4. 딕셔너리 = dict({'키1': 값1, '키2': 값2})

# 1.의 예시
lux1 = dict(health = 490, mana = 334, melee = 550, armor = 18.72)
print(lux1)

# 2의 예시
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'],[490,334,550,18.72]))
print(lux2)

# 3의 예시
lux3 = dict([('health', 490),('mana',334),('melee',550),('armor',18.72)])
print(lux3)

# 4의 예시
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print(lux4)

# 딕셔너리의 키에 접근해보기
print(lux['health'])
print(lux2['armor'])

# 참고로 그냥 키를 지정안하면 전체가나옴
print(lux3)

# 이제 딕셔너리의 키에 값 할당해보기

lux['health'] = 2037  # lux의 키 'health'의 값을 2037로 변경
lux3['mana'] = 1184 # lux3 의 'mana'의 값을 1184로 변경

print(lux)
print(lux3)

# 딕셔너리에 새로운 키와 값 할당해보기

lux['mana_regen'] = 3.28
print(lux)

# 딕셔너리에 내가 찾는 키가 있는지 True or False로 확인해보기

print('health' in lux)
print('hello' in lux3)

# 반대로 in 앞에 not을 붙이면 특정 키가 없는지 확인

print('attack_speed' not in lux) # 'attack_speed' 라는 키는 없으니 True반환

# 딕셔너리의 개수(키의 갯수) 구해보기

print(len(lux))
print(len(lux3))


