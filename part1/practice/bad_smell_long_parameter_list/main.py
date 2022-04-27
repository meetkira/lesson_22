# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, x: int, y: int, speed: int = 1):
        self.field = Field()
        self.x = x
        self.y = y
        self.speed = speed

    def _set_move_type(self, move_type):
        self.move_type = move_type

    def _set_speed(self):
        if self.move_type == "fly":
            self.speed *= 1.2
        elif self.move_type == "crawl":
            self.speed *= 0.5
        else:
            print("wrong move_type")

    def move(self, move_type: str, direction: str):
        self._set_move_type(move_type)
        self._set_speed()
        if direction == 'UP':
            self.field.set_unit(x=self.x, y=self.y + self.speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=self.x, y=self.y - self.speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=self.x - self.speed, y=self.y, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(x=self.x + self.speed, y=self.y, unit=self)
        else:
            print("wrong direction")


class Field:
    def set_unit(self, x: int, y: int, unit: Unit):
        pass
