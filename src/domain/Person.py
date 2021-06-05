class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        return self.name

    @property
    def age(self) -> int:
        return self.age
