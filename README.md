# Paycheck Calculator | using Python
---
### Reason for the Application:
I get paid on a weekly basis and I was interested in a creating something using python that would take in the amount of of what I get paid and subtract the expenses that I have for that upcoming week. This would let me know how much money I have left of to either invest, save or spend. 
### Results: 
Using Treehouse courses and some Youtube as references I created a simple program that will ask for users input in several cases to then run through a `if` statement that would ask the user if they were sure the amound inputted was correct if not re prompt a new input. If the user was correct in inputting their numbers the program would the subtract one input againts the other. 
### Challenges:
1. When coding this at first I had some issues with the indention of the if statement and having some syntax error. Once those issues were fixed, I was able to run the application throughout right before the mathematical part. 
2. I looked up how to make a basic calculation using python on Youtube and saw that since the user was inputting a `str` and not and `int` I needed to convert that in order for the math portion to work out. The solution was the following `str(int(pay_amount) - int(bills_to_pay))`. This understood that the input the user was giving would be a string and I would have to take that `str` and make it and `int` for both the pay ammount and the bill ammount that needed to be paid. 
3. Decimals. I found that when I was using the code with whole numbers I was able to run it with no issues. However, when I tested using decimals I immediately broke the application. I got the `ValueError: invalid literal for int() with base 10` 
---
### Improvements:
- There might be a way to clean up the code by using a function. This is something that I am aware of and need to keep coding in order to fully understand how I can make a function and I am able to understand it. 
- It would be also cool to have the program remember the input for the amount that was paid for if this is a recurring same amount paycheck all I would technically need to add is the amount of bills due for that week which would be different
---
### Coding Journey Journal: 
So far I have spent about two weeks coding on a schedule, Saturdays tend to be my build days and I felt very happy that this code actually work. It made me feel like if I can keep pushing with using the concept of building programs as I learn, I will be able to understand my learning more and feel accomplished with that learning mindset. 
