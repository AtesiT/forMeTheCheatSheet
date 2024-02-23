class Car():
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def create(self):
        print(f'Ваша {self.name} с цветом {self.color} {str(self.year)} года выпуска, ожидает в гараже')

    def carAge(self):
        print(f'Вашей машине {2024-int(self.year)} год(ов)')


class SportCar(Car):
    def __init__(self, name, color, year, speed):
        super().__init__(name, color, year)
        self.speed = speed

    def returnSpeed(self):
        print(self.speed)

carPorshe = Car('Porshe', 'красный', '2023')
carPorshe.create()
print(carPorshe.color)
carPorshe.carAge()


ferrari = SportCar('Ferrari', 'yellow', '2016', '500')
ferrari.returnSpeed()
ferrari.carAge()