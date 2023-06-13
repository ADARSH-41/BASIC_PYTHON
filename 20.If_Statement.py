#In python if statement is a conditional statement which executes only after the given condition evaluates to true

discount = 0
amount = int(input('Enter the Amount to be paid : '))
if amount>1000:
    discount = amount*0.1
print("Discount on your purchase is : %f"%discount)
print("You have to pay a sum of %f"%(amount-discount))