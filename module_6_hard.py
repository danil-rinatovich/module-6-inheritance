import math


class Figure:
    sides_count = 0

    def __init__(self, sides: int, color, filled: bool):
        self.__sides = []
        self.__color = []
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return (isinstance(r, int) and 0 <= r <= 255
                and isinstance(g, int) and 0 <= g <= 255
                and isinstance(b, int) and 0 <= b <= 255)

    def set_color(self, r, g, b):
        if not self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.sides_count != len(new_sides):
            self.sides_count = len(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color, filled, radius):
        super().__init__(sides, color, filled)
        self.__radius = radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)

    def get_square(self):
        return 


class Cube(Figure):
    sides_count = 12

    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        self.__sides = 12

    def get_volume(self):
        return self.__sides ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
