def multipleAtoB(a, b):
    return a*b

print(multipleAtoB(2,4))

lambdaMultipleAtoB = lambda a, b: a * b
print(lambdaMultipleAtoB(2, 4))

print((lambda a, b: a * b)(2, 4))


def whichIsNumberBigger(a, b):
    if a > b:
        return a
    else:
        return b


lambdaWhichIsNumberBigger = (lambda a, b: a if a > b else b)