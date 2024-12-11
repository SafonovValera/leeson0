class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __eq__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

    def __gt__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor

    def __lt__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor

    def __ne__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3
print(House.houses_history)
