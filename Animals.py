
class Animal:
    def __init__(self, eat, weight, sound, name):
        self.eat = eat
        self.weight = weight
        self.sound = sound
        self.name = name

    def eating(self, time):
        self.weight += self.eat * time

    def weighting(self, new_weight):
        self.weight = new_weight


class Bird(Animal):
    egg = 1

    def collecting(self, quantity):
        return self.egg * quantity


class Beast(Animal):
    milk = 10

    def milking(self, time):
        return self.milk * time  # л в час


class Geese(Bird, Animal):
    sound = 'Га га га'


class Cow(Beast, Animal):
    sound = 'МУУ'


class Sheep(Animal):
    sound = 'Беее'
    wool = 1

    def hair_shearing(self, time):
        return self.wool * time   # кг шерсти в час


class Chicken(Bird, Animal):
    sound = 'Ко ко ко'


class Goat(Beast, Animal):
    sound = 'Mee'
    milk = 5


class Duck(Bird, Animal):
    sound = 'Кря'


geese_1 = Geese(1, 2, 'Га га', 'Серый')
geese_2 = Geese(1, 2, 'Га га', 'Белый')

cow = Cow(8, 200, 'Мууу', 'Манька')

sheep_1 = Sheep(3, 90, 'Бее', 'Барашек')
sheep_2 = Sheep(4, 86, 'Бее', 'Кудрявый')

chicken_1 = Chicken(1, 3, 'Кудах', 'Ко-Ко')
chicken_2 = Chicken(1, 3, 'Кудах', 'Кукареку')

goat_1 = Goat(3, 80, 'Мее', 'Рога')
goat_2 = Goat(3, 90, 'Мее', 'Копыто')

duck = Duck(2, 3, 'Кря', 'Кряква')

geese_1.eating(5)
geese_2.eating(5)
cow.eating(5)
sheep_1.eating(5)
sheep_2.eating(5)
chicken_1.eating(5)
chicken_2.eating(5)
goat_1.eating(5)
goat_2.eating(5)
duck.eating(5)
print(goat_2.milking(3), 'л молока')
print(cow.milking(3), 'л молока')
print(sheep_1.hair_shearing(2), 'кг шерсти')
print(chicken_1.collecting(20), 'яиц')

animals_dict = {geese_1.name: geese_1.weight, geese_2.name: geese_2.weight, cow.name: cow.weight,
                sheep_1.name: sheep_1.weight, sheep_2.name: sheep_2.weight,
                chicken_1.name: chicken_1.weight, chicken_2.name: chicken_2.weight,
                goat_1.name: goat_1.weight, goat_2.name: goat_2.weight, duck.name: duck.weight
                }

count = 0
for weight_animal in animals_dict.values():
    count += weight_animal
print(f'Общий вес животных {count} килограмм')

max_count = 0
animal_id = 0
for i, y in animals_dict.items():
    if max_count < y:
        max_count = y
        animal_id = i
print(f'{animal_id} самое тяжелое животное весом в {max_count} кг')
