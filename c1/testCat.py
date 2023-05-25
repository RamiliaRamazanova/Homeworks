from cat import Cat

class Dog(Cat):
    def get_pet(self):
        return self.get_name(), self.get_age()

dog1 =Dog('Boll', 'M', 7)

print(dog1.get_pet())