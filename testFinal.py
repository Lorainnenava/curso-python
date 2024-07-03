# names = ["Anna", "Natasha", "Mike"]
# names.insert(2, "Xi")
# print(names)

# for x in range(1, 4):
#     print(int((str((float(x))))))

# def recursion(num):
#     print(num)
#     next = num - 3
#     if next > 1:
#         recursion(next)

# recursion(11)

# num = 9
# class Car:
#     num = 5
#     bathrooms = 2

# def cost_evaluation(num):
#     num = 10
#     return num

# class Bike():
#     num = 11

# cost_evaluation(num)
# car = Car()
# bike = Bike()
# car.num = 7
# Car.num = 2
# print(num)

def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()