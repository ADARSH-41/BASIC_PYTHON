
'''Bitwise Operators do the bitwise operations on each bit'''

a = 62
b = 60
print('a = ',a,' : ',bin(a),' b = ',b,' : ',bin(b))
c = 0

c = a & b; #AND Operation
print('Result of AND operation is = ',c,' : ',bin(c))

c = a|b; #OR Operation
print('Result of OR operation is = %d : %s'%(c,bin(c)))

c = a^b; #XOR Operation
print('Result of XOR operation is = %d : %s'%(c,bin(c)))

c = a>>b #Right Shift
print('Result of Right Shift operation is = %d :  %s'%(c,bin(c)))

c = a<<b #Left Shift
print('Result of Left Shift Operation is = %d : %s'%(c,bin(c)))



