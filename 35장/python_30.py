# Unit 35 . 클래스 속성과 정적, 클래스 메서드 사용하기

# 클래스 속성과 인스턴스 속성 알아보기

# 인스턴스 속성 = __init__

# 클래스속성은 그럼??

# class 클래스 이름:
#   속성 = 값


class Person:
  bag = []
  
  def put_bag(self,stuff):
    self.bag.append(stuff)
    
james = Person()
james.put_bag("책")

maria = Person()
maria.put_bag("열쇠")

print(james.bag)
print(maria.bag)

# 클래스 속성은 같은 클래스에 속해있다면 모든 인스턴스는 그걸 공유한다.


# put_bag 메서드에서 클래스 속성 bag에 접근할 떄 "self"를 사용했다. >> 조금 모호
# 그럼 Person.bag.append(stuff) >> 클래스이름으로 클래스속성에 접근해보자 >> 이름 아 이건 Person클래스의 속성에 접근한다 라고 명시

# 그럼 가방에 각각 따로 넣으려면?

class Person:
  def __init__(self):
    self.bag = [] # 그냥 인스턴스 속성을 만들어버리면 됨
    
  def bag_put(self,stuff):
    self.bag.append(stuff)
    
james = Person()
james.bag_put("책")

maria = Person()
maria.bag_put("연필")

print(james.bag)
print(maria.bag)


# 비공개 클래스 속성이다 이번엔

class Knight:
  __item_limit = 10 # 비공개 클래스 속성
  
  def print_item_limit(self):
    print(Knight.__item_limit) # 클래스 안에서만 접근가능
    
    
x = Knight()
x.print_item_limit() # 10

# print(Knight.__item_limit) # 이렇게 밖에선 접근안댐


# 정적 메서드 사용해보기

# 지금까지는 클래스의 메서드를 사용할 때 인스턴스를 통해서 호출해보았다.
# 이번에는 인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있는 정적 메서드와 클래스 메서드에 대해 알아보겠다.

# 먼저 정적메서드, self안씀

# class 클래스 이름
#   @staticmethod
#   def 메서드(매개변수1, 매개변수2):
#     코드


class Calc:
  @staticmethod
  def add(a,b):
    print(a + b)
  
  @staticmethod
  def minus(a,b):
    print(a - b)
    
Calc.minus(10,5)
Calc.add(3,6)

# 정적 메서드와 비슷하지만 약간의 차이점이 있는 클래스 메서드를 사용해보자

# class 클래스이름:
#   @classmethod
#   def 메서드(cls, 매개변수1, 매개변수2):
#     코드


class Person:
  count = 0 # 클래스속성 count 선언후 0으로 초기화
  
  def __init__(self):
    Person.count += 1 # 인스턴스가 만들어질 때
                      # 클래스 속성 count에 1을 더함
  
  @classmethod
  def print_count(cls):
    print("{0}명 생성되었음".format(cls.count)) # cls로 클래스 속성에 접근
    
james = Person()
maira = Person()

Person.print_count()

class Date:
  @staticmethod
  def is_date_valid(date_string):
    year,month,day = map(int,date_string.split('-'))
    return month <= 12 and day <= 31
  
if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')



class Time:
  def __init__(self,hour,minute,second):
    self.hour = hour
    self.minute = minute
    self.second = second
  
  def from_string(time_string):
    hour,minute,second = map(int,time_string.split(':'))
    return hour,minute,second

  
  @staticmethod  
  def is_time_valid(time_string):
    hour,minute,second = map(int,time_string.split(':'))
    return hour <= 24 and minute < 60 and second <= 60
  
    

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else: 
    print('잘못된 시간 형식입니다.')