h = int(input())

for i in range(h):
  for j in range(h-i-1): # 공백을 몇개찍을래?
    print(" ",end='')
  for k in range(2*i+1): # 공백을 다 찍었는데 이제 별찍어야지? 몇개찍을건데?
    print("*",end='')
  print()
    
# i가 기준이니까 조건자체에 i를 계속 쓴다