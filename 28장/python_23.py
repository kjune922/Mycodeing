# Unit 28. 회문 판별과 N-gram 만들기
# 문자열을 응용해서 회문을 판별하는 방법과 N-gram만드는 방법 알아보기

# 회문 판별

# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어 or 문장
# ex) "level", "SOS" 등등

# 우선 문자열이 회문인지 판별하려면??
# 1. 첫번째 글자와 마지막 글자가 같다
# 2. 안쪽으로 한 글자씩 좁혔을 때 글자가 서로 같으면 = 회문이다

    

word = input("단어를 입력하세요: ")
print(len(word))
print(len(word)//2)
print(word[-1-1]) # -1을 하면 할수록 문자열왼쪽에서 오른쪽으로간다
print(word[-1]) # 문자열의 맨끝에있는 문자
print(word[-5])
print(word[0])
print(word[6])
is_paline = True
for i in range(len(word) // 2): # 0부터 문자열 길이의 절반만큼 반복
  if word[i] != word[-1-i]: # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
    is_paline = False # 회문이 아님
    break
print(is_paline) #  회문 판별값 출력

