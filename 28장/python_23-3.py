# 연습문제
n = int(input())
text = input()
words = text.split()

if len(words) < n:
  print('wrong')
else:
  n_gram = zip(*[words[i:] for i in range(n)])
  for i in n_gram:
    print(i)
    
is_paline = True
    
with open("words.txt",'r') as file:
  for line in file:
    words = line.strip('\n')
    if words == words[::-1]:
      print(words)