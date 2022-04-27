# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self, room_number: int, city_population: int):
        self._room_number = room_number
        self._city_population = city_population

    def get_person_room(self):
        return self._room_number

    def get_city_population(self):
        return self._city_population

# после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.
if __name__ == "__main__":
    person = Person(room_number=1, city_population=150000)
    print(person.get_person_room())
    print(person.get_city_population())