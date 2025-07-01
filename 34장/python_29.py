# Unit 34. 클래스 사용하기

# 특정한 개념이나 모양으로 존재하는 것을 "객체(object)" 라고 부른다.
# 프로그래밍으로 객체를 만들 때 사용하는 것이 클래스 입니다.

# ex ) 게임의 기사 캐릭터를 클래스로 표현
# 체력, 마나, 물리 공격력 ... ->> 클래스의 속성
# 베기, 찌르기 등의 스킬 ... ->> 메서드

# 클래스와 메서드 만들어보기

class Person: # class 클래스이름
  def greeting(self): # def 메서드(self):
    print('Hello') # 코드(행동, 행위)
    
james = Person() # james가 Person의 "인스턴스"
james.greeting() # 메서드 호출


# 다음과 같이 리스트를 조작할 때 메서드를 사용했었죠??
# 인스턴스 b 에서 메서드 append를 호출해서 값을 추가합니다.
# 이 부분도 지금까지 메서드를 만들고 사용한 것과 같은 방식임

b = list(range(10))
b.append(20) # 메서드 append
print(b)


# 인스턴스와 객체의 차이점??

# 클래스는 객체를 표현하는 문법이라고 했는데, 클래스로 인스턴스를 만든다니 좀 헷갈린다
# 사실 인스턴스와 객체는 같은 것을 뜻함

# 참고) 메서드 안에서 메서드 호출하기

class Person:
  def greeting(self):
    print("Hello")
    
  def hello(self):
    self.greeting()  # self.메서드() 형식으로 클래스 안의 메서드를 호출
    
james = Person()
james.hello()
james.greeting()

# 특정 클래스의 인스턴스인지 확인해보기

class Person:
  pass

james = Person()
print(isinstance(james,Person))

# isinstance는 주로 객체의 자료형을 판단할 때 사용한다.

def factorial(n):
  if not isinstance(n,int) or n < 0: # n이 정수형이 아니거나, 0보다 작으면 그냥 끝냄
    return None
  if n == 1:
    return 1
  return n * factorial(n-1)

a = factorial(4)
print(a)

# 이번에는 클래스에서 속성을 만들고 사용해보자
# 속성(attribute)을 만들 때는 __init__ 메서드 안에서 self.속성에 값을 할당한다.

# class 클래스이름:
#   def __init__(self):
#       self.속성 = 값


class Person():
  def __init__(self):
    self.hello = "안녕하세용"
    
  def greeting(self):
    print(self.hello)
    
james = Person()
print(james.greeting())

# __init__ 메서드는 james = Person() 처럼 클래스에 "()"를 붙여서 인스턴스를 만들 때 호출되는 특별한 메서드이다

# 그냥 한마디로 self.속성 = "여기에 값을 할당할걸 적는다"

# self의 의미??

# self는 인스턴스 자기 자신을 의미한다.


# 이제 인스턴스를 만들 때 값 받기


class Person:
  def __init__(self,name,age,address):
    self.hello = "안녕하세요"
    self.name = name
    self.age = age
    self.address = address
    
  def greeting(self):
    print('{0} 저는 {1}입니다'.format(self.hello,self.name))
    
james = Person("제임스", 27, "부산시 해운대구")
james.greeting()
print("이름:",james.name)
print("나이:",james.age)
print("주소:",james.address)    # 이렇게 self가 아니고 인스턴스를 통해 접근하는 속성을 "인스턴스 속성" 이라고 한다.


# 참고

class Perosn:
  def __init__(self,*args):
    self.name = args[0]
    self.age = args[1]
    self.address = args[2]
    
maria = Person(*['마리아',27,"부산시 수영구"])
print(maria.name)
print(maria.age)
print(maria.address)

# 번외로
# 클래스에서 __slots__ 에 허용할 속성 이름을 리스트에 넣어주면, 넣은애들만 속성으로 허용한다. 인스턴스 호출하고 속성을 리스트내용말고는 불가능

# 비공개 속성 사용해보기

# private attribute

# 비공개 속성은 __속성 과 같이 이름이 __(밑줄이 두개)로 시작해야댐

# class 클래스 이름:
#   def __init__(self,매개변수)
#     self.__속성 = 값

# Person클래스에 지갑을 추가로 넣어보자 비공개로

class Person():
  def __init__(self,name,age,address,wallet):
    self.name = name
    self.age = age
    self.address = address
    self.__wallet = wallet
    
maria = Person("마리아",28,"창원시",10000)
# maria.__wallet -= 10000 # 이렇게 클래스 바깥에서 비공개 속성에 접근하면 에러발생

# 그럼이제 Pay메서드를 만들어보자
# 왜냐하면 비공개 속성은 클래스안의 메서드만이 접근가능

class Person():
  def __init__(self,name,age,address,wallet):
    self.name = name
    self.age = age
    self.address = address
    self.__wallet = wallet
    
  def pay(self,amount):
    if amount > self.__wallet: # 사용하려고하는 금액보다 지갑에 든 돈이 적을때
      print("돈 없누...")
      return
    self.__wallet -= amount # 비공개 속성은 클래스 안의 메서드에서만 접근가능
    print("이제 {0}원 남았네 ㅋ".format(self.__wallet))
    
maria = Person("마리아",25,"서울강남",10000)
maria.pay(5000)
maria.pay(3000)
maria.pay(2000)
maria.pay(500)

# 연습문제 : 게임 캐릭터 클래스 만들기

class Annie():
  def __init__(self,health,mana,ability_power):
    self.health = health
    self.mana = mana
    self.ability_power = ability_power
    
  def tibbers(self):
    print("티버: 피해량",self.ability_power * 0.65 + 400)
    
health, mana, ability_power = map(float, input().split())
 
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()