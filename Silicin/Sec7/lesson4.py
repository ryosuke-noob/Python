class Person(object):

    kind = 'human' # 全てのオブジェクトで共有されるため，リストなどの扱いは気を付ける必要がある

    def __init__(self, name):
        # self.kind = 'human'
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

class T(object):
    def __init__(self) -> None:
        self.words = []
    
    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')

d = T()
d.add_word('add 3')
d.add_word('add 4')

print(c.words)
print(d.words)