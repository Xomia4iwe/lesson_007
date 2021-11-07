# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Mud()

    def __str__(self):
        return self.__class__.__name__


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Earth):
            return Dust()
        if isinstance(other, Water):
            return Storm()

    def __str__(self):
        return self.__class__.__name__


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Air):
            return Lightning()
        if isinstance(other, Water):
            return Steam()

    def __str__(self):
        return self.__class__.__name__


class Earth:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Water):
            return Mud()
        if isinstance(other, Air):
            return Dust()

    def __str__(self):
        return self.__class__.__name__


class Lava:
    def __str__(self):
        return self.__class__.__name__


class Lightning:
    def __str__(self):
        return self.__class__.__name__


class Steam:
    def __str__(self):
        return self.__class__.__name__


class Mud:
    def __str__(self):
        return self.__class__.__name__


class Dust:
    def __str__(self):
        return self.__class__.__name__


class Storm:
    def __str__(self):
        return self.__class__.__name__


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Earth() + Fire())