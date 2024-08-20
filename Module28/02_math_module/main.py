# TODO здесь писать код
import math
class MyMath:
    @classmethod
    def circle_len(cls, radius):
        return math.pi * (radius * 2)

    @classmethod
    def square_circle(cls, radius):
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, side_length):
        return side_length ** 3

    @classmethod
    def sphere_surface_area(cls, radius):
        return 4 * math.pi * radius ** 2

    @classmethod
    def rhombus_volume(cls, base_area, height):
        return (1/3) * base_area * height

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.square_circle(radius=6)
res_3 = MyMath.cube_volume(side_length=7)
res_4 = MyMath.sphere_surface_area(radius=8)
res_5 = MyMath.rhombus_volume(base_area=4, height=5)

print(res_1)
print(res_2)
print(res_3)
print(res_4)
print(res_5)