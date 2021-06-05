class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name: str):
        if not isinstance(self.name, str):
            raise TypeError('Argument name is not type str')
        self.name = name

    @property
    def age(self) -> int:
        return self.age

    @age.setter
    def age(self, age: int):
        if not isinstance(self.age, int):
            raise TypeError('Argument age is not type int')
        self.age = age
