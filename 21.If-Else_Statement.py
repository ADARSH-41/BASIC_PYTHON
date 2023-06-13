'''In python If-Else statement is the conditional statement, which has an alternative
to execute another block of statements incase of if condition evaluates to false'''
discount = 0
amount = int(input("Enter the amount to be paid : "))
if amount>1000:
    discount = amount * 0.1
else:
    discount = amount * 0.05

print("The savings you made : ",discount)
print("The total amount you have to pay : ",(amount-discount))