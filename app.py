from random import choice


class Person:

    def __init__(self, name):
        self.greeting = 'Hello {name}'
        self.name = name

    def make_greeting(self):
        return self.greeting.format(name=self.name)

    def __str__(self):
        return self.make_greeting()


def main():

    people = [
        Person('Name 1'),
        Person('Name 2'),
        Person('Name 4'),
        Person('Name 4')
    ]
    person = choice(people)
    print(person)


if __name__ == '__main__':
    main()