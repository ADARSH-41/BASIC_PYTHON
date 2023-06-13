a = 20
b = a

print("a = ",a,":",id(a), "b = ",b,":",id(b))
if a is b:
    print('a and b have the same identity')
else:
    print('a and b do not have the same identity')

if(id(a) == id(b)):
    print('a and b have the same identity')
else:
    print('a and b do not have the ssame identity')

b = 30
print('a =',a,':',id(a),'b =',b,':',id(b))
if a is not b:
    print('a and b not have the same identity')
else:
    print('a and b have the same identity')

