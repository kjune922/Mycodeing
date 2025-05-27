# 문자열에서 내가 원하는 단어만 찾아보기
# 정확히 찾고싶으면 단어 경계를 인식하게 만들어야됨
# 그럼 그냥 어떤 길다란 문맥을 받고 전부다 소문자로 낮춘다음
# split()으로 리스트를 만들어 단어단계로 구분함
# 그리고 the만 뽑아냄




x = input()
x = x.lower().split()
count = 0
for i in x:
  words = i.strip(',.')
  print(words)
  if words == 'the':
    count+=1
print(count)

# 문자열을 입력받고, lower로 소문자로 만들고, 
# 이 문자열을 split()으로 리스트로 만들고 
# 이제 for문을써서 리스트안에서 한개씩 꺼내서 인덱스0부터 the랑 일치하는지 확인해서 
# count를 세고, 최종적 count를 출력

x = list(map(int,input().split(';')))
x.sort(reverse=True)
for i in x:
  print("{0:>9,}".format(i))
