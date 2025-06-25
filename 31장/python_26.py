# Unit 31. 함수에서 재귀호출 사용하기

# def hello():
  # print('Hello, world!')
  # hello()
  
# hello()

# 이렇게 실행하면 이론상 무한으로 출력하는데, 마지막에 에러가뜨는이유는 파이썬자체에서 재귀깊이를 1000으로 제한하기때문

# 그래서 재귀호출에서 종료조건은 필수다

def hello(count):
  if count == 0:
    return
  print("hello, wordl!",count)
  
  count -= 1 # count를 1 감소시킨뒤
  hello(count) # 다시 hello에 넣음
  
hello(5)

# 재귀호출을 사용해서 팩토리얼을 구현해보자

def factorial(n):
  if n == 1: # n이 1일 때
    return 1 # 1을 반환하고 재귀를 끝낸다
  return n * factorial(n-1) # n과 factorial 함수에 n-1을 넣어서 반환된 값을 곱함

print(factorial(5))

# 재귀호출로 회문

def is_palindrome(word):
  if len(word) < 2:
    return True
  if word[0] != word[-1]:
    return False
  return is_palindrome(word[1:-1])

# 피보나치 회문

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))