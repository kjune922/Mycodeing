# 반복문으로 딕셔너리의 키-값 쌍 모두 출력해보기
x = {'a':10,'b':20,'c':30,'d':40}
for i in x:
  print(i,end='')
print()
# 다음은 for로 딕셔너리x의 모든 키와 값 출력

for key,value in x.items():
  print(key,value)
print()
# for 키,값 in 딕셔너리.items():
  # 반복할 코드

# 딕셔너리 키만 출력하기
for key in x.keys():
  print(key)
print()  
 
# 딕셔너리 값만 출력하기  
for value in x.values():
  print(value)
print()

# 딕셔너리 표현식 사용하기:: 딕셔너리 컴프리핸션
# 리스트와 마찬가지로 딕셔너리도 for 반복문과 if 조건문을 사용해서 딕셔너리 생성가능
# {키: 값 for 키, 값 in 딕셔너리}
# dict{키: 값 for 키, 값 in 딕셔너리}
keys = ['a','b','c','d']
x = {key:value for key, value in dict.fromkeys(keys).items()}
print(x)

# 이처럼 딕셔너리 표현식을 사용할 때는 for in 다음에 딕셔너리를 지정하고, items를 사용한다
# 그리고 키, 값을 가져온 뒤에는 키:값 형식으로 변수나 값을 배치하여 딕셔너리를 생성하면 된다.

# x = {key: value for key, value in dict.fromkeys(리스트변수명).items()}
# dict.fromkeys(리스트변수명).items()로 키-값 쌍을 구한 뒤 키는 변수key, 값은 변수 value에 꺼내고 최종적으로 key와 value를 이용해 딕셔너리 만듬

x = {key:0 for key in dict.fromkeys(keys).keys()}
print(x)
keys = {'a':10,'b':20,'c':30,'d':40}
# 키와 값 서로 바꿀수도있음
x = {value:key for key, value in {'a':10,'b':20,'c':30,'d':40}.items()}
print(x)
x=  {value:key for key, value in keys.items()}
print(x)

# 딕셔너리 표현식에서 if 조건문 사용해보기
# 딕셔너리 표현식은 딕셔너리에서 특정 값을 찾아서 삭제하기좋다

x = {'a':10,'b':20,'c':30,'d':40}

# 딕셔너리는 for반복문으로 삭제가 불가능하다!
# for key, value in x.items():
#  if value == 20: # 값이 20이면
#    del x[key]
# print(x)

# 그래서 딕셔너리 컴프리핸션을 쓴다
x = {key:value for key,value in x.items() if value != 20}
print(x)

# 딕셔너리 안에서 딕셔너리 사용해보기
# 다음과 같이 딕셔너리는 값 부분에 다시 딕셔너리가 계속 들어갈 수 있다
# 딕셔너리 = {키1: {키A: 값A}, 키2: {키B: 값B}}

terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
 
print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8

# 딕셔너리 terrestrial_planet에 키 'Mercury', 'Venus', 'Earth', 'Mars'가 들어있고
# 이 키들은 다시 값 부분에 딕셔너리를 가지고 있습니다. 즉, 중첩 딕셔너리는 계층형 데이터를 저장할 때 유용하다

# 딕셔너리 안에 들어 있는 딕셔너리에 접근하려면 딕셔너리 뒤에 [](대괄호)를 단계만큼 붙이고 키를 지정해주면 됨

# 딕셔너리[키][키]
# 딕셔너리[키][키] = 값

# 예를들어 금성(Venus)의 반지름(mean_radius)를 출력하려면 다음과 같이 먼저 'Venus'를 찾아가고 다시 'mean_radius'의 값을 가져오면 된다.

print(terrestrial_planet['Venus']['mean_radius'])
print(terrestrial_planet['Earth']['mean_radius'])

# 딕셔너리의 할당과 복사

x = {'a':0,'b':0,'c':0,'d':0}
y = x
print(x is y)

y['a'] = 99
print(x)
print(y)

y = x.copy()
print(x is y)
print(x == y)
y['a'] = 0

print(x)
print(y)

# 중첩 딕셔너리의 할당과 복사 알아보기
x = {'a':{'python': '2.7'},'b':{'python':'3.6'}}
y = x.copy()
print(x is y)

y['a']['python'] = '2.7.15'
print(x)
print(y)

# 왜 시발 애는 똑같이 copy()했는데 할당처럼 딕셔너리요소가 같이바뀌지?? 뭐냐

# 암튼 서로 다르게 완벽하게 복사할라면
import copy # copy 모듈가져오기
y = copy.deepcopy(x)
y['a']['python'] = '2.7'
print(x)
print(y)