# Unit 27. 파일 사용하기

# 파일에 문자열 쓰기, 읽기
# 파일에 문자열 써보기

# 파일객체 = open(파일 이름, 파일모드)
# 파일객체.write('문자열')
# 파일객체.close()

file = open("hello.txt",'w') # hello.txt파일을 쓰기모드(w)로 열기, 파일 객체 반환
file.write("Hello, world!!") # 파일에 문자열 저장
file.close() # 파일객체 닫기

# 이제 파일에서 문자열 읽기
# 읽기모드 "r" 사용

file = open("hello.txt",'r') # hello.txt파일을 읽기모드(r)로 열기, 파일 객체 반환
s = file.read() # 파일에서 문자열 읽기
print(s) # Hellom world! 출력
file.close() # 파일객체 닫기

# 매번 close()로 닫으려니 좀 귀찮음 ㅋ
# 그럴땐 with open(파일이름, 파일모드) as 파일객체: >> 파일을 사용한 뒤 자동으로 파일 객체를 닫아준다

with open("hello.txt","r") as file:
  s = file.read()
  print(s)
  
# 반복문으로 문자열 여러 줄을 파일에 쓰기
# 앞에선 문자열 한 줄을 파일에 썼는데 문자열 여러 줄은 어떻게 쓰면 될까?? 간단하게 반복문으로 해결 ㄱㄴ

with open("hello.txt","w") as file:
  for i in range(3): # 3줄출력하겠다 > 3번반복
    file.write("Hello, world! from LEE {0}\n". format(i)) # "\n" 은 개행문자이다, 엔터키담당

# 리스트에 들어있는 문자열을 파일에 써보자

lines = ['안녕하세요 \n', "파이썬\n", "코딩 도장입니다잉.\n"]

with open("hello.txt",'w') as file:
  file.writelines(lines)
  
  # writelines는 리스트에 들어있는 문자열을 그대로 파일에 쓰게해준다, 그리고 writelines를 쓸떄, 리스트요소마다 개행문자 "\n"을 꼭 넣어야한다

with open("hello.txt","r") as file:
  s = file.readlines()
  print(s)
  
# 파일의 내용을 

# readlines말고 readline으로 한줄씩 읽을려면 while을 써야함
# while line != '': 라는 조건을 걸어서 빈문자열이 아닐떄 계속 반복해서 출력하도록 만들어준다

with open("hello.txt","r") as file:
  s = None # 변수 s는 while로 반복하기전에 무조건 None으로 초기화해야함
  while s != "":
    s = file.readline()
    print(s.strip('\n')) # 파일에서 읽어온 문자열에서 \n을 삭제해서 출력
    

# while로 할라니 좀 정신사나움
# 그래서 파이썬은 for를 많이쓴다

with open("hello.txt", "r") as file: # 우선 읽기모드로 열고
  for line in file: # 파일속 내용을 line에 한줄씩담는다
    print(line.strip('\n')) # 그리고 원래넣었던 개행문자열을 삭제해주고 한줄씩 출력
    

# 파일에서 문자열만 읽고 쓰면 느낌 x
# 파이썬은 객체를 파일에 저장하는 pickle 모듈을 제공해준다

# 파이썬 객체를 파일에 저장하는 과정 >> pickling 피클링

# 파일에서 객체를 읽어오는 과정 >> unpickling 언피클링 

import pickle

name = "james"
age = 27
address = "부산시 사하구 하단동"
scores = {'korean': 90, "englis": 95, "mathmatics" : 88, "science": 90}

with open('james.p','wb') as file: # james.p 라는 파일을 "wb"즉 바이너리 쓰기 모드로 연다
  pickle.dump(name,file)
  pickle.dump(age,file)
  pickle.dump(address,file)
  pickle.dump(scores,file)
  
# 확장자를 p로한거는 우리가 pickling할거라서 p를했음 다른거 해도 ㄱㅊ
# james.p를 들어가면 ㅈ같이 보이는데 이건 바이너리 파일이라는게 컴퓨터가 처리하는 파일이라
# 사람이 못알아봄 ㅋ


# 파일에서 파이썬 객체 읽어오기
with open('james.p','rb') as file:
  name = pickle.load(file)
  age = pickle.load(file)
  address = pickle.load(file)
  scores = pickle.load(file)
  print(name)
  print(age)
  print(address)
  print(scores)

# 앞에서 james.p 를 피클링할때 pickle.dump를 4번 썼음
# 그럼 언피클링할려고 읽어올때도 pickle.load를 4번써야함 ㅋ
# 순서도 그대로 가져오면 됨 ㅇㅇ

