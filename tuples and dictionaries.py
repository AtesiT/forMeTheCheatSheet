#кортеж - не изменяется
newTuple = ('element', 10, 50.0,)
print(newTuple)
print(list(newTuple))

anyDictionary = {
    'phone': '101-500',
    'city': "New York",
    'country': "United States"
}
#выводит phone, city, country
for i in anyDictionary.keys():
    print(i)

#выводит 101-500, New York, United States
for i in anyDictionary.values():
    print(i)

anyDictionary['city'] = 'Miami'
del(anyDictionary['phone'])

#вывести всё
for i in anyDictionary.items():
    print(i)

