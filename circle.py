data = [10, 501, 22, 37, 100, 999, 87, 351]
class Circle:
    __pi = 3.141
    def __init__(self, data):
        self.data = data
    def datas(self):
        print(self.data)
    def area_of_circle(self, radius):
        area = self.__pi * radius * radius
        return area

    def perimeter_of_circle(self, radius):
        perimeter = 2 * self.__pi * radius
        return perimeter

d = Circle(data)
d.datas()
for i in data:
    print("area of circle when radius is ", i, d.area_of_circle(i))
    print("perimeter of circle when radius is ", i, d.perimeter_of_circle(i))

