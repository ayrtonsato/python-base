"""
exemplo de programação funcional + declarativa
people = [{
    "name": "Jim Halpert",
    "balance": 500,
    "role": "Salesman"
},
{
    "name": "Dwight Schrute",
    "balance": 100,
    "role": "Manager"
}]


# modo funcional
# pure functions - no side effects
def add_points(person, value):
    data = person.copy() # no side effects
    if data["role"] == "Manager":
        value *= 2
    data["balance"] += value
    return data


result = map(lambda person: add_points(person, 100), people)
# modo funcional
# declarativa
# lazy evaluation

print(list(result))
"""

# Classe `class` - MaterialDeEscritorio, Eletronico, Gadget, Fruta
# Objetos - intancias criadas a partir da classe - caneta, relogio, banana
# Atributos - valores definidos nas classes e nos objetos
# Método - Função definida no escopo da classe


class Person: # pascalCase, UpperCamelCase
    """Represents a person."""
    company_name = "Dunder Mifflin" # snake_case
    work_address = "Rua Stanton, Pensilvania"
    balance = 0

    # Data Model - Método Dunder, Métodos Mágicos
    def __init__(self, name, role="Undefined", prefered_colors=None):
        self.name = name
        self.role = role
        self.prefered_colors = prefered_colors or []

    # nunca defina um valor mutavel como atributo de classe
    # prefered_colors = [] # classe mutável

    # Injeção de dependência - 1 arg método = a própria instância
    def add_points(self, value): # método / snake_case
        """Add points to balance"""
        if self.role == "Manager":
            value *= 2
        self.balance += value

jim = Person(
    name="Jim Halpert",
    role="Salesman",
    prefered_colors=["Blue"]
) # Person.__prepare__();Person.__new__() (construtor)
# __init__ (inicializador da classe)
jim.add_points(100)
print(jim.name, jim.balance, jim.prefered_colors, jim.role)
print()

pam = Person(name="Pam Belsey", prefered_colors=["Purple"])
pam.add_points(100)
print(pam.name, pam.balance, pam.prefered_colors, pam.role)
print()

print(Person.__dict__)
