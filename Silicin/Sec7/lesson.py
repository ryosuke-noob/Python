class Person(object):
    def __init__(self, name) -> None:
        self.name = name
    
    def say_something(self):
        print(f'I am {self.name}. Hello!')
        self.run(10)
    
    def run(self, num):
        print('run' * num)

    def __del__(self):
        print('Good bye')

if __name__ == '__main__':
    person = Person('Mike')
    person.say_something()

    del person

    print('################')