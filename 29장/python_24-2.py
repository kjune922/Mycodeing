# 함수 스택다이어그램 알아보기

def mul(a,b):
  c = a*b
  return c

def add(a,b):
  c = a+b
  print(c)
  d = mul(a,b)
  print(d)
  
x = 10
y = 20
print(add(x,y))


# 연습문제 1

x = 10
y = 3

def get_quotient_remainder(a,b):
  return a // b, a%b

quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))

# 심사문제

x,y = map(int,input().split())



def calc(a,b):
  return a + b, a - b, a * b, a / b

a,s,m,d = calc(x,y)
print("덧셈: {0}, 뺼셈: {1}, 곱셉: {2}, 나눗셈: {3}".format(a,s,m,d))