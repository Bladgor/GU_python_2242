
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        if self.speed > 0:
            print(f'Машина {self.name} уже в движении')
        else:
            self.speed = speed
            print(f'Машина {self.name} начала движение')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')
        if self.speed > 60:
            print('Внимание! Превышение скорости.')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')
        if self.speed > 40:
            print(f'Внимание! У машины {self.name} превышение скорости.')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(speed=0, color='Yellow', name='Bus_1', is_police=False)
town_car.go(30)
town_car.turn('налево')
town_car.show_speed()

sport_car = SportCar(speed=150, color='Red', name='Flash', is_police=False)
sport_car.show_speed()
sport_car.stop()
sport_car.show_speed()

work_car = WorkCar(speed=50, color='Grey', name='Garbage_truck', is_police=False)
work_car.show_speed()

police_car = PoliceCar(speed=100, color='White', name='Judge', is_police=True)
print(f'Полицейский автомобиль {police_car.name} едет со скоростью {police_car.speed}')
