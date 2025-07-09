# Unit 39. 이터레이터 사용하기

# 이터레이터(iterator)는 값을 차례대로 꺼낼 수 있는 객체(object)입니다.

# 지금까지 for반복문을 사용할 때 range를 사용해습니다. 만약 100번 반복한다면 for i in range(100): 처럼
# 만들었습니다.


it = [1,2,3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())


a = "Hello, world!".__iter__()
print(a.__next__())

for i in range(3):# 여기서 range(3)은 반복 가능한 객체, -> __iter__() -> __next__() = 0 -> __next__() = 1 ... 2까지
  print(i)
  
# 이처럼 반복 가능한 객체는 __iter__ 메서드로 이터레이터를 얻고, 이터레이터의 __next__메서드로 반복한다.

# 리스트, 튜플, range, 문자열은 반복 가능한 객체이면서 시퀀스 객체이다.
# 하지만, 딕셔너리와 세트는 반복 가능한 객체이지만 시퀀스 객체는 아니다.

# 시퀀스 객체는 요소의 순서가 정해져있고 연속적으로 이어져야함
# 요소의 순서와 상관없이 요소를 한번에 하나씩 꺼낼 수 있으면 반복 가능한 객체



# 이제 __iter__, __next__ 메서드를 구현해서 직접 이터레이터 만들어보기
# 간단하게 range(횟수)처럼 동작하는 이터레이터임.

class Counter:
  def __init__(self,stop):
    self.current = 0 # 현재 숫자유지, 0부터 지정된 숫자 직전까지 반복
    self.stop = stop # 반복을 끝낼 숫자
  
  def __iter__(self):
    return self # 현재 인스턴스 반환
  
  def __next__(self):
    if self.current < self.stop:
      r = self.current
      self.current += 1
      return r
    else:
      raise StopIteration
    
for i in Counter(3):
  print(i, end = ' ')
  

# 지금까진 __iter__와 __next__ 메서드를 구현하는 방식으로 이터레이터를 만들었다. 이번에는 "__getitem__" 메서드를 구현하여
# 인덱스로 접근할 수 있는 이터레이터를 만들어보겠다.

# 앞에서 만든 Counter 이터레이터를 인덱스로 접근할 수 있도록 다시 만들어보겠다.
print()

class Counter:
  def __init__(self,stop):
    self.stop = stop
    
  def __getitem__(self,index):
    if index < self.stop:
      return index * 10
    else:
      raise IndexError

print(Counter(3)[0],Counter(3)[1],Counter(3)[2])
for i in Counter(3):
  print(i, end = ' ')
  

# 파이썬 내장 함수 iter, next 에 대해 알아보겠습니다. iter는 객체의 __iter__ 메서드를 호출해주고, next는
# 객체의 __next__메서드를 호출해준다. 그럼 range(3)에 iter와 next를 사용해보겠다

print()
it = iter(range(3))

print(next(it))
print(next(it))
print(next(it))


# iter

# iter(호출가능한 객체, 반복을 끝낼 값)

import random
it = iter(lambda : random.randint(0,5),2) # 0부터 5까지 무작위로 숫자 생성할 때 2가 나오면 반복을 끝낸다는 뜻
# 그리고 호출가능한 객체를 넣어야하니까 lambda 씀

# 이거를 for에 활용하면됨 

import random

for i in iter(lambda : random.randint(0,5),2):
  print(i, end = ' ')
  
# next

# next는 기본값을 지정할 수 있습니다. 기본값을 지정하면 반복이 끝나더라도 StopIteration이 발생하지 않고 기본값을 출력
# 즉, 반복할 수 있을 때는 해당 값을 출력하고, 반복이 끝나면 기본값 출력

# range(3)으로 0,1,2 세번 반복하는데 next에 기본값으로 10을 지정한 것
print()

it = iter(range(3))
print(next(it,10))
print(next(it,10))
print(next(it,10))
print(next(it,10))
print(next(it,10))


class MultipleIterator:
  def __init__(self,stop,multiple):
    self.multiple = multiple
    self.stop = stop
    self.cuurent = 0
  def __iter__(self):
    return self
  
  def __next__(self):
    self.cuurent += 1
    if self.cuurent * self.multiple < self.stop:
      return self.cuurent * self.multiple
    else:
      raise StopIteration
    
for i in MultipleIterator(20, 3):
    print(i, end=' ')
 
print()
for i in MultipleIterator(30, 5):
    print(i, end=' ')

print()
    
class TimeIterator:
  def __init__(self,start,stop):
    self.stop = stop
    self.start = start
        
  def __getitem__(self,index):
    if self.start + index < self.stop:
      total_seconds = self.start + index
      h = (total_seconds // 3600) % 24
      m = (total_seconds % 3600) // 60
      s = (total_seconds % 60)
      return f"{h:02}:{m:02}:{s:02}"
    else:
      raise IndexError
    
    
start, stop, index = map(int, input().split())
 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')