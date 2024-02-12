def sumOfElements(*anyArgs):
    print(sum(anyArgs))

sumOfElements(5, 6, 7, 8, 9, 10, 11, 12)



def returnAllElements(**kwargs):
    print(kwargs.items())

returnAllElements(a = 'Apple',
                  b = 'Banana',
                  c = 'Cake')

def returnAllElementsToo(**kwargs):
    for x, y in kwargs.items():
        print(x, ':', y)

returnAllElementsToo(a = 'Apple',
                     b = 'Banana',
                     c = 'Cake')

