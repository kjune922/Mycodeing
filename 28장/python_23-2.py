# 시퀀스 뒤집기로 문자 검사하기

word = input("단어 입력하셈: ")

print(word == word[::-1]) # 원래문자열과 반대로 뒤집은 문자열 비교
# ㅅㅂ 뭐야이거 ㅈㄴ쉽네

# 리스트와 reversed 사용하기

word = 'level'
print(list(word) == list(reversed(word)))

# 문자열의 join 메서드와 reversed 사용하기

word = 'SOS'
word == ''.join(reversed(word))

# N-gram 만들기

# 문자열에서 N개의 연속된 요소를 추출하는 방법
# 만약 "Hello"라는 문자열을 문자(글자)단위 2-gram으로 추출하면 다음과 같이 된다

text = 'Hello'

for i in range(len(text) - 1):
  print(text[i],text[i+1], sep='')

# 만약 3-gram이라면 반복횟수는 (len(text) - 2) 가 된다

# 글자 단위 N-gram이 있다면, 단어 단위 N-gram도 있겠죠?
text = 'this is python script'
words = text.split()

for i in range(len(words) - 1):
  print(words[i],words[i+1])
  
# zip으로 2-gram 만들어보기

text = 'hello'

two_gram = zip(text, text[1:])
for i in two_gram:
  print(i[0],i[1],sep='')
  
# 단어 단위

text = "this is python script"

words = text.split()
print(list(zip(words,words[1:]))) # 2-gram

# 3-gram
print(list(zip(words,words[1:],words[2:]))) # 3-gram

# 4-gram
print(list(zip(words,words[1:],words[2:],words[3:])))

# zip과 리스트 표현식으로 N-gram 만들기

text = "hello"
a = list(zip(*[text[i:]for i in range(3)]))
print(a)

# 이렇게만하면 3-gram이 아니다 >> 서로 콤마로 