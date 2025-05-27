# 문자열 서식 지정자와 포매팅 사용하기

# 서식 지정자 (format specifier)로 문자열 중간에 다른 문자열 넣어보기

# %s == %"문자열" 이라는 의미 여기서 s는 string의 s다

print("I am %s." %"James")

name = 'maria'
print("I am %s." %name)

# %d == %숫자 , d == decimal integer의 d <정수>

print("I am %dyears old."%20)

# %f == %소수 , f == fixed point <소수>

print("My score is %f."%85.123) # 소수좀 6자리까지 표현한다

# 만약 소수점 이하 자릿수를 지정하고 싶다면??
print("My score is %.3f"%85.1)

# 서식 지정자로 문자열 정렬하기

# %길이s

print("%10s" %'Python')

# 왼쪽으로 붙여보기
print("%-10s"%'Python')

# 서식 지정자로 문자열 안에 값 여러 개 넣기

print("Please give me %d %s" %(3, "apples"))

# format 메서드 사용해보기

print("Hello, {}".format("world!"))

print("Hello, {}".format(100))

# format 메서드로 값을 여러개 넣기

print("Hello, {0}{2}{1}".format("Java",3.5,"Script")) # 여기서 {0}{2}{1}은 리스트 0 1 2 순서임

# format 메서드로 같은 값을 여러 개 넣기

print("{0}{0}{1}{1}".format("Hello","World"))

# format 메서드에서 인덱스대신에 이름 넣어서 안헷갈리기

print("Hello, {programing} {version}".format(programing = 'Java Script',version= 3.5))

# 문자열 포매팅에 변수를 그대로 사용하기

language = 'C++'
version = 17

print(f'Hello, {language} {version}')

# 중괄호 자체를 쓰고싶을때는 두번쓰셈요 ㅋ

print("Hello, {{{0}}}".format('Python')) # {겉에꺼 기본깔고{한번더 깔고 {0 우리가 넣을 인덱스}}} 총 3개쓴다잉 

# format 메서드로 문자열 정렬

# '{인덱스:<길이}'.format(값)

print("{0:<010}".format('Python')) # 값을 총길이가 10인곳에서 왼쪽에 붙여 정렬하고 나머지를 0으로 채운다

print("{0:>010}".format('Python')) # 값을 총길이가 10인곳에서 오른쪽에 붙여 정렬하고 나머지 0으로 채움

# 숫자 갯수 맞춰넣기

print("%03d" %5) # 000 이라는 길이 3짜리에 5를넣는
print("{0:05d}".format(35)) # 00000에 35를 넣는

print("{0:010d}".format(12345))

# 실수 버젼

# %0갯수.자릿수f % 숫자
# "{인덱스:0개수.자릿수f}".format(실수)
print("%08.03f" %3.3)
print("{0:08.2f}".format(5.27))
print("{0:08.5f}".format(1.23))

# 채우기와 정렬을 조합해서 사용해보기
# "{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}" ㅆ발 이게뭐야

print("{0:0<10}".format(15)) # 길이 10, 왼쪽정렬후 남은곳 0
print("{0:0>10}".format(15)) # 길이 10, 오른쪽정렬후 남은곳 0

# 실수버전
print("{0:0>10.2f}".format(3.5)) # "."포함 길이 10, 소수점이하는 2칸까지 그리고 나머진 0

# 개꿀팁 큰 숫자 천단위로 콤마넣기
print(format(148434090,','))


print("%20s"%format(1448348,',')) # 총길이가 20이다

print("{0:0>20,}".format(2833928389230119))