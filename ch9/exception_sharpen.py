try:
    num = input('Got a number? ')
    result = 42 / int(num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Excuse me, we asked for a number.")
else:
    print('Your answer is', result)
finally:
    print('Thanks for stopping by.')
