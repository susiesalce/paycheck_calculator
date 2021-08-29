print("How much did you get paid:\n")
pay_amount = input()
print("Awesome! You got paid ${} dollars".format(pay_amount))

print("What is the sum of your bills that needs to be payed with the paycheck")
bills_to_pay = input()
print("You currently have {} bills to pay. Is this correct? Y/N".format(bills_to_pay))
response = input ()  
if response == 'Y':
    print("The left over money is $" + str(round(float(pay_amount) - float(bills_to_pay), 2)) + " dollars. Happy spending!")
elif response == 'N':
    print("Please input the correct amount ammount")
    bills_to_pay = input()
    print("The left over money is $" + str(int(pay_amount) - int(bills_to_pay)) + " dollars. Happy spending!")
else: 
    print("invalid input")
