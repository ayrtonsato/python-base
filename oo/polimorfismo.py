# Polimorfismo

class Dog:
    def make_sound(self):
        return "woof woof"

class Cat:
    def make_sound(self):
        return "meow meow"

def print_sound(obj): # Soundable
    # implementa make_sound
    if not hasattr(obj, "make_sound"):
        raise TypeError(f"{obj} is not soundable")
    print(obj.make_sound())

rex = Dog()
print_sound(rex)

lili = Cat()
print_sound(lili)

# Duck Typing
"""
Se o objeto anda como um pato,
parece um pato, faz quack como um pato,
então é um pato!
"""


def funcao(*args):
    ret = 0
    for arg in args:
        ret += arg
    return ret
