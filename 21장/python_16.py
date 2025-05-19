# Unit 21. 터틀 그래픽스로 그림그리기

import turtle as t
t.shape('turtle')


# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)

# for i in range(4):
#  t.forward(100)
#  t.right(90)

n = int(input())
t.color('red') # 펜의 색을 빨간색으로 설정


t.begin_fill()
for i in range(n): # 오각형이므로 5번 반복 , n이면 n번반복
  t.forward(100)
  t.right(360/n) # 360을 5로 나누어서 외각을 구한다 , n으로 나누는게 n각형을 만듬
t.end_fill()


t.mainloop()



