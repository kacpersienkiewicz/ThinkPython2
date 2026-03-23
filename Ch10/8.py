'''
Exercise 10.8. This exercise pertains to the so-called Birthday Paradox, which you can read about
at http: // en. wikipedia. org/ wiki/ Birthday_ paradox .
If there are 23 students in your class, what are the chances that two of them have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for
matches. Hint: you can generate random birthdays with the randint function in the random
module.
You can download my solution from https: // thinkpython. com/ code/ birthday. py .
'''
import random
birthdays = []

for i in range(23):
    birthdays.append(random.randint(1,365))

birthdays.sort()

for i in range(len(birthdays) - 1):
    if birthdays[i] == birthdays[i + 1]:
        print("Birthday Paradox confirmed.")
