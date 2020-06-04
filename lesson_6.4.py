class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехал'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} = {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Теукщая скорость городского автомобиля {self.name} = {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше допустимой'
        else:
            return f'Скорость {self.name} в пределах нормы'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} = {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше допустимой'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} находится в расположении полиции'
        else:
            return f'{self.name} находится не в расположении полиции'


Doodge = SportCar(100, 'Red', 'Doodge', False)
VAZ = TownCar(30, 'White', 'VAZ', False)
Ford = WorkCar(70, 'Green', 'Ford', True)
UAZ = PoliceCar(110, 'Blue',  'UAZ', True)
print(Ford.turn_left())
print(f'Когда {VAZ.turn_right()}, то {Doodge.stop()}')
print(f'{Ford.go()} со скоростью {Ford.show_speed()}')
print(f'{Ford.name} = {Ford.color}')
print(f'{Doodge.name} полицейский автомобиль? {Doodge.is_police}')
print(f'{Ford.name}  полицейский автомобиль? {Ford.is_police}')
print(Doodge.show_speed())
print(VAZ.show_speed())
print(UAZ.police())
print(UAZ.show_speed())