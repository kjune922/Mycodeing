# 지뢰찾기

# 2차원리스트의 가로(col)와 세로(row)가 입력되고
# 그 다음줄부터 리스트의 요소로 들어갈 문자가 입력
# 이때, 2차원 리스트의 "*"은 지뢰이고 "."은 지뢰가 아니다
# 지뢰가 아닌 요소에는 인접한 지뢰의 갯수를 출력하는 프로그램 만들어보기
# 인접한 지뢰의 갯수는 위아래 대각선까지해서 3x3정사각형을 인접한 위치라고 본다


# 2차원리스트 생성

col,row = map(int,input().split())

matrix = []
# for  i in range(col):
for j in range(row):
  matrix.append(list(input()))

# 2차원리스트 꺼내서 출력

for i in range(len(matrix)): # 한마디로 행을 도는것 row
  for j in range(len(matrix[i])): # 한마디로 1행의 열을 도는거니까 col
    if matrix[i][j] == "*":
      continue
    else:
      matrix[i][j] = 0 # 0을 넣어서 요소 주변의 8곳을 둘러보고 *을 발견할때마다 +1
      for x in range(i-1,i+2):
        for y in range(j-1,j+2):
          if x < 0 or y < 0 or x >= row or y >= col: # 행이나 열이 0일때 음수가되는걸 계산하는걸 방지하는 코드
            
            
            continue
          elif matrix[x][y] == "*":
            matrix[i][j] += 1

for i in range(row): # 행을 도는것
  for j in range(col): # 열을 도는 것
    print(matrix[i][j],end='')
  print()
  

# 추가로 for문 속 range를 이해하기위해
i = 1
for x in range(i-1, i+2):
    print(x)

# 여기서
# 0
# 1
# 2 

# 이렇게 출력이 이루어지는데, for문 속에 range는 (0,3) 이렇게 범위가 되어있다면,
# 0, 1, 2 이렇게 3번만함
# 그래서 i-1부터 i+1까지 검사를 하고싶다면, i-1부터 i+2가 범위가 되어야한다.