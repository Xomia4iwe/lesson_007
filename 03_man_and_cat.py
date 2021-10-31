# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой коту'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('Нет еды для кота'.format(self.name), color='red')

    def clean_the_house(self):
        self.house.mess -= 100
        self.fullness -= 20
        if self.house.mess < 0:
            self.house.mess = 0
        cprint('Убирать в доме еще рано!'.format(self.name), color='red')

    def eat(self):
        if self.house.food >= 20:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 20
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def pick_up_cat(self, cat):
        self.cat = cat
        cprint('{} взял кота {}!'.format(self.name, self.cat.name), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.fullness < 10:
            self.eat()
        elif self.house.food <= 30:
            self.shopping()
        elif self.house.cat_food < 10:
            self.buy_cat_food()
        elif (self.house.money < 50 or self.house.cat_food < 50 or self.house.food < 20) and not self.house.mess > 100:
            self.work()
        elif self.house.mess >= 50:
            self.clean_the_house()
        else:
            self.watch_MTV()


class Cat:
    def __init__(self, name, house=None):
        self.name = name
        self.fullness = 50
        self.house = house

    def __str__(self):
        return 'Сытость кота {}'.format(self.fullness)

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} спал целый день'.format(self.name), color='green')

    def eat(self):
        if self.house.cat_food >= 10:
            self.fullness += 20
            self.house.cat_food -= 10
            cprint('Кот {} поел'.format(self.name), color='yellow')
        else:
            cprint('У кота {} нет еды'.format(self.name), color='red')

    def rips_wallpaper(self):
        self.fullness -= 10
        self.house.mess += 5
        cprint('Кот {} рвал обои'.format(self.name), color='green')

    def cat_go_to_the_house(self, house):
        self.house = house
        cprint('{} кота принесли в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('Кот {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        else:
            self.rips_wallpaper()


class House:

    def __init__(self):
        self.food = 50
        self.money = 50
        self.cat_food = 0
        self.mess = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды для кота осталось {}, кот навел беспорядка {}'.format(
            self.food, self.money, self.cat_food, self.mess)


man = Man(name='Гриша')
my_sweet_home = House()
cat = Cat(name='Угрюмый', house=my_sweet_home)
man.pick_up_cat(cat=cat)
man.go_to_the_house(house=my_sweet_home)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    man.act()
    cat.act()
    cprint('--- в конце дня ---', color='blue')
    cprint(man, color='magenta')
    cprint(cat, color='magenta')
    cprint(my_sweet_home, color='cyan')

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
