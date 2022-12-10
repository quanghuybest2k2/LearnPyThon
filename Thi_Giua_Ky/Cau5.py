class Animal:
    def __init__(self, name: str, age: int, gender: str):
        self._name = name;
        self.age = age;
        self.gender = gender;

    def __str__(self) -> str:
        return "Tên: {}\nTuổi: {}\nGiống: {}".format(self.name, self.age, self.gender);

    @property
    def name(self) -> str:
        return self._name;

    @staticmethod
    def sound() -> str:
        pass;

class Dog(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender);

    @staticmethod
    def sound() -> str:
        return "Gâu gâu";


class Cat(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender);

    @staticmethod
    def sound() -> str:
        return "Meo meo";

class Animals():
    def __init__(self, list: list):
        self.list = list;

    def add(self, animal: Animal):
        self.list.append(animal);

    def averageAge(self):
        return sum([animal.age for animal in self.list]) / len(self.list);

# dog = Dog('Dog1', 3, 'Đực');
# cat = Cat('Cat1', 2, 'Cái');
# animals = Animals([]);
# animals.add(dog);
# # dog.name = "new name";
# animals.add(cat);
# print(cat);
# print(cat.sound());
# print('-------');
# print(dog);
# print(dog.sound());
# print("Số tuổi trung bình của các con vật trong danh sách: {}".format(animals.averageAge()));