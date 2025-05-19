import turtle as t
"""
t.shape('turtle')
t.circle(120)

n = 60
t.shape('turtle')
t.speed('fastest') # 거북이 속도를 가장 빠르게 설정
for i in range(n):
  t.circle(120) # 반지름이 120인 원 그림
  t.right(360 / n)  # 오른쪽으로 6도 회전
  
"""
"""

t.shape('turtle')
t.speed('fastest') # 거북이 속도 젤 빠르게
for i in range(300): # 300번 반복
  t.forward(i)  # i만큼 앞으로 이동, 반복할때마다 선이길어짐
  t.right(91) # 오른쪽으로 91도 회전

"""

n, line = map(int, input().split())

t.shape('turtle')
t.speed('fastest')
for i in range(n):
  t.forward(line)
  t.right(360/n * 2)
  t.forward(line)
  t.left(360/n)
  
t.mainloop()