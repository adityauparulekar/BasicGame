import random
class Obj():
    def __init__(self):
        self.a = 1

class Col():
    def __init__(self):
        self.b = [Obj() for i in range(4)]

    def print_obj(self):
        for B in self.b:
            print(B.a)


class Oth():
    col = Col()
    def __init__(self):
        self.collection = random.sample(Oth.col.b, 2)

    def modify(self):
        self.collection[0].a = 2

o = Oth()
Oth.col.print_obj()
o.modify()
Oth.col.print_obj()
