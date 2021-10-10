a = int(input('a='))
b = int(input('b='))
amal = input('add/sub/mul/div:')
if amal == 'add':
    c = a + b
elif amal == 'sub':
    c = a - b
elif amal == 'mul':
    c = a * b
elif amal == 'div':
    c = a / b
else:
    c = 'Error'
print('Result = ', c)
