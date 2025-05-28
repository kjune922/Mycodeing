maria = {"korean": 94,"englis":91,"mathmatics":89,"science":83}
average = sum(maria.values())/len(maria)
print(average)

keys = input().split()
values = map(int, input().split())
x = dict(zip(keys,values))
x.pop('delta')
x = {key:value for key,value in x.items() if value != 30}
print(x)

