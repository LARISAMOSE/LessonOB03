import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе.")

    def eat(self):
        print(f"{self.name} ест.")


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает.")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит.")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")


class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member.name} добавлен в зоопарк.")

    def show_animals(self):
        print(f"Животные в зоопарке {self.name}:")
        for animal in self.animals:
            print(f"{animal.name}, возраст: {animal.age}")

    def show_staff(self):
        print(f"Сотрудники в зоопарке {self.name}:")
        for staff in self.staff:
            print(f"{staff.name}, должность: {staff.position}")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Состояние зоопарка сохранено в файл {filename}.")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                zoo = pickle.load(file)
            print(f"Состояние зоопарка загружено из файла {filename}.")
            return zoo
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Возвращаем новый зоопарк.")
            return Zoo("Новый Зоопарк")


# Создаем зоопарк
zoo = Zoo("Городской Зоопарк")

# Добавляем животных
bird = Bird("Попугай", 2, "20 см")
mammal = Mammal("Лев", 5, "золотистый")
reptile = Reptile("Змея", 3, "гладкая")

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

# Добавляем сотрудников
keeper = ZooKeeper("Иван")
vet = Veterinarian("Доктор Сидоров")

zoo.add_staff(keeper)
zoo.add_staff(vet)

# Показать животных и сотрудников
zoo.show_animals()
zoo.show_staff()

# Используем методы сотрудников
keeper.feed_animal(bird)
vet.heal_animal(mammal)

# Сохранение состояния зоопарка в файл
filename = "zoo_state.pkl"
zoo.save_to_file(filename)

# Загрузка состояния зоопарка из файла
loaded_zoo = Zoo.load_from_file(filename)
loaded_zoo.show_animals()
loaded_zoo.show_staff()
