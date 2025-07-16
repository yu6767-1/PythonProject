class Car:
    def __init__(self,name,typed):
        self.name=name
        self.typed=typed
    def driving(self):
        print(f"这是{self.name}车")
    def distance(self):
        print(f"车的类型为{self.typed}")
        distanced = input("输入车行驶的距离为多少公里：")
        print(distanced)
my_car=Car("奥迪A6","轿车")
my_car.driving()
my_car.distance()
your_car=Car("路虎","商务车")
your_car.driving()
your_car.distance()
print('1')