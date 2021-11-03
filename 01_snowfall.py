# -*- coding: utf-8 -*-

import simple_draw as sd
import random as r

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат


class Snowflake:

    def __init__(self):
        self.x = r.randint(100, 1000)
        self.y = r.randint(550, 600)
        self.length = r.randint(10, 25)
        self.start_point = sd.Point(self.x, self.y)
        self.flag_can_fall = False

    def clear_previous_picture(self):
        sd.snowflake(center=self.start_point, length=self.length, color=sd.background_color)

    def move(self):
        if self.y - self.length >= 0:
            self.y -= 10
            self.x -= sd.random_number(-5, 5)
            self.start_point = sd.Point(self.x, self.y)
        else:
            self.flag_can_fall = True
            self.y -= 0
            self.start_point = sd.Point(self.x, self.y)

    def draw(self):
        sd.snowflake(center=self.start_point, length=self.length, color=sd.COLOR_WHITE)

    def can_fall(self):
        if self.flag_can_fall:
            return False
        return True


flake = Snowflake()


# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
def get_flakes(count):
    snowfall = []
    for _ in range(count):
        new_snowflake = Snowflake()
        snowfall.append(new_snowflake)
    return snowfall


def get_fallen_flakes():
    fallen_snowflakes = []

    for number_of_fallen_snowflakes, flake in enumerate(flakes):
        if flake.y < 10:
            fallen_snowflakes.append(number_of_fallen_snowflakes)
    for delta, index in enumerate(fallen_snowflakes):
        flakes.pop(index - delta)
    return len(fallen_snowflakes)


def append_flakes(count):
    for _ in range(count):
        new_snowflake = Snowflake()
        flakes.append(new_snowflake)


flakes = get_flakes(count=10)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
