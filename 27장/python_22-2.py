with open("words.txt","r") as file:
  for line in file:
    s = line.split()
  for word in s:
    result = word.strip(",.")
    if "c" in result:
      print(result)
      
