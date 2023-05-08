import random


class Animal(object):
  def __init__(self, species: str, age:int=0):
    self._species = species
    self._age = age or random.randint(1, 100)

  def get_species(self) -> str:
    return self._species

  def get_age(self) -> int:
    return self._age

  def get_complex_object(self):
    return random.Random()

  def __str__(self):
    return '%s:%s' % (self._species, self._age)



class Pet(Animal):
    def __init__(self, name : str, *args):
        Animal.__init__(self, *args)
        self._name = name

    def get_name(self) -> str:
        return self._name

    @staticmethod
    def lower(s: str) -> str:
        return s.lower()

    def __str__(self):
        return '%s is a %s aged %d' % (
            self.get_name(), 
            Pet.lower(self.get_species()), self.get_age()
        )


def create_pet(name: str, species: str, age: int=0):
    return Pet(name, species, age)


if __name__ == '__main__':
    print(Pet('Polly', 'Parrot'))
    print(create_pet('Clifford', 'Dog', 32))