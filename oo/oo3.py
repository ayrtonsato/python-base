class Triangle:
    side_qtd = 3

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """Calcula a área de um triângulo"""
        perimeter = self.a + self.b + self.c
        s = perimeter / 2
        area = s * (s - self.a) * (s - self.b) * (s - self.c)
        return area ** 0.5 # math.sqrt(area)

triangulos = [
    Triangle(3, 4, 5),
    Triangle(5, 12 ,13),
    Triangle(8, 15 , 17),
    Triangle(12, 35, 37)
]

for t in triangulos:
    print("A area do triangulo é: ", t.area())
