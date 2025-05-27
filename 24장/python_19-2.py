# 메서드 체이닝

# 이렇게 문자열 메서드는 처리한 결과를 반환하도록 만들어져 있다
# 따라서 메서드를 계속 연결해서 호출하는 메서드 체이닝이 가능
# 메서드 체이닝은 메서드를 줄줄이 연결한다고 해서 메서드 체이닝이라고 부른다
# 다음은 문자열을 오른쪽으로 정렬한 뒤, 대문자로 바꿈

print('python'.rjust(10).upper())

# 사실 문자열을 입력받을 때 자주 사용했던 input().split()도 input()이 반환한 문자열에
# split을 호출하는 메서드 체이닝이다

# 문자열 왼쪽에 "0" 채워보기

# zfill(길이)는 지정된 길이에 맞춰서 문자열 왼쪽에 0을 채운다 (zfill == zero fill)
print('35'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(10))

# 문자열 위치 찾기

# find('찾을 문자열)은 문자열에서 특정 문자열을 찾아서 씨발인덱스위치였구나를 반환하고, 문자열이 없으면 -1을 반환
# find는 왼쪽에서부터 문자열을 찾는데, 같은게 여러개일땐 왼쪽에서 처음찾은거 반환

print('apple pineapple'.find('pl'))

print('apple pineapple'.find('xy'))

# 오른쪽에서 부터 찾기

print('apple pineapple'.rfind('pl'))

print('apple pineapple'.rfind('xy'))

# 문자열 위치만 찾기

print('apple pineapple'.index('pl')) # 왼쪽에서부터찾음
# 애는 문자열없으면 -1이 아니고 error내뱉음

print('apple pineapple'.rindex('pl'))

# 문자열 갯수 세기

# count('문자열')은 현재 문자열에서 특정 문자열이 몇 번 나오는지 알아낸다

print('apple pineapple'.count('p'))