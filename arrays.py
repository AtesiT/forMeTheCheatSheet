fruits = ['apple', 'banana', 'mango', 'orange']
print(fruits.pop())
print(fruits)
# ['apple', 'banana', 'mango']
print(fruits.append('kiwi'))
print(fruits)
#узнать индекс элемнта, а затем длину
print(fruits.index('banana'))
print(len(fruits))

numbers = [51, 12, 41, 1, 62, 14, 23, 105, 8]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

