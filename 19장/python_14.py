# Unit 19. 중첩 루프 사용해보기

# 계단식으로 별 출력하기

a = int(input())

for i in range(a):
  for j in range(a):
    print('j:',j,sep='',end=' ')
  print('i:',i,'\\n',sep='')
  
a = int(input()) # 몇줄? 

for i in range(a):
  for j in range(a):
    if j <= i: # 세로 방향 변수 i만큼
      print("*",end=' ') # 별 출력, end에 ' ' 를 지정해서 줄바꿈안함
  print()
  
# 한마디로, 바깥쪽 루프의 i가 세로방향, 안쪽 루프의 j가 가로방향을 처리