# 2020.02.13
# Inhefitance and composition (188~199)
from abc import ABC


class Engine:  # 엔진 클래스는 시작 정지 함수를 가지고 있다.
    def start(self):
        pass

    def stop(self):
        pass

class DieselEngine(Engine):  # 디젤 엔진은 엔진의 속성을 상속받는다. isA Engine
    pass

class GasolineEngine(Engine):  # 가솔린 엔진도 엔진의 속성을 상속 받는다. isA Engine
    pass

class Car:  # 차량 클래스는
    engine_cls = Engine  # 엔진클래스를 attribute로 가지고 있게 된다.

    def __init__(self):
        self.engine = self.engine_cls()  # 엔진을 초기화 한다. hasA Engine

    def start(self):
        print(
            'Starting engine {} for car {}... Wroom, wroom!'
            .format(self.engine.__class__.__name__, self.__class__.__name__)
            # 엔진 명과 차량 클래스의 이름이 출력된다.
        )
        self.engine.start()

    def stop(self):
        self.engine.stop()

class RaceCar(Car):  # RaceCar 는 Car 클래스를 상속받고 isA Car
    engine_cls = GasolineEngine  # 가솔린 엔진을 쓰는 것으로 한다.

class SUVCar(Car):  # SUVCar 는 Car 클래스를 상속받고 isA Car
    engine_cls = DieselEngine  # 디젤 엔진을 쓰는 것으로 한다.

class F1Car(Car):  # isA Car
    engine_cls = GasolineEngine

car = Car()
racecar = RaceCar()
suvcar = SUVCar()
f1car = F1Car()
cars = [car, racecar, suvcar, f1car]
cars_tuple = [(car, 'car'), (racecar, 'racecar'), (suvcar, 'suvcar'), (f1car, 'f1car')]
cars_class = [Car, RaceCar, SUVCar, F1Car]

for c in cars:
    c.start()

for car, carname in cars_tuple:
    for carcls in cars_class:
        belongs = isinstance(car, carcls)
        msg = 'is a' if belongs else 'is not a'
        print(carname, msg, carcls.__name__)

for carcls1 in cars_class:
    for carcls2 in cars_class:
        subclass = issubclass(carcls1, carcls2)
        msg = 'is a subclass of' if subclass else 'is not a subclass of'
        print(carcls1.__name__, msg, carcls2.__name__)

print('-'*30)

# Base class 사용법
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class EBook(Book):
    def __init__(self, title, publisher, pages, format_):
        # Book.__init__(self, title, publisher, pages)   # Book 관련 속성은 이렇게 초기화 한다.
        super().__init__(title, publisher, pages)  # 하지만 그냥 super()를 통해 부모를 호출할 수 있다.
        self.format_ = format_


# Multiple inheritance
#             object
#         Shape    Plotter
#             Polygon
#         Regular Polygon
#   Regular Hexagon    Square
class Shape:
    geometric_type = 'Generic Shape'

    def area(self): # This acts as placeholder for the interface
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:
    def plot(self, ratio, topleft):
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon(Shape, Plotter):  # base class for polygons
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):  # Is-A Polygon
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularHexagon(RegularPolygon):  # Is-A RegularPolygon
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(RegularPolygon):  # Is-A RegularPolygon
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side

hexagon = RegularHexagon(10)
print(hexagon.area())  # 259.8076211353316
print(hexagon.get_geometric_type())  # RegularHexagon
hexagon.plot(0.8, (75, 77))  # Plotting at (75, 77), ratio 0.8.

square = Square(12)
print(square.area())  # 144
print(square.get_geometric_type())  # Square
square.plot(0.93, (74, 75))  # Plotting at (74, 75), ratio 0.93.

print('-'*30)

# 위와 같은 Multiple inheritance 상황에서 특정 attribute를 찾아가려 하는데
# 호출 된 클래스에 attr가 없으면 상위 클래스로 하나씩 올라가면서 찾게 된다.
# 이때 찾아가는 순서를 지정해 줄 수 있는게 Method resolution order이다.

print(square.__class__.__mro__)  # 위에서 만든 도형 관련 클래스의 Method resolution order
