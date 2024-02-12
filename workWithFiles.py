with open('1.txt', 'w') as somethingName:
    somethingName.write('Example')
#w - write
#a - add
#r - read

f = open('1.txt', 'r')
print(f.read())
f.close()


try:
    a = int(input('Enter any number: '))
    b = int(input('Enter any number. Will be better zero: '))
    print(a / b)
except ZeroDivisionError:
    print('You trying to divide by zero. Not good')