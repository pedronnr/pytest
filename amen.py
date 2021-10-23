class Car:
    def __init__(self):
        self.wheels = 4
        self.color = "blue"

    def getColor(self):
        return "rodas: " + str(self.wheels) + " | cor: " + self.color


car = Car()

print(car.getColor())