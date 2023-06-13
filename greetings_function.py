def func():
    global greeting
    greeting = 'Hello World'
    return greeting

func()
print(greeting)

#map(function,*iterator)

j = [1,2,3,0]
lst = []
for i in j:
    lst.append(int(i))
print('c for loop : ',lst)

def square(i):
    return int(i)*2

map_obj = map(square,j)
print('map : ',list(map_obj))
