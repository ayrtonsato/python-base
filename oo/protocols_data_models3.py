# Protocols / Data Models
from protocols_data_models2 import Verde, Azul, Vermelho # noqa


nome = "Ayrton"  # str # Iterable - __iter__
for letra in nome:
    print(letra)

print(list(nome))

# Collection -> Sized + Container + Iterable


class Paleta:
    def __init__(self, *cores) -> None:
        self._cores = cores

    # Iterable
    def __iter__(self):
        return iter([cor.icon for cor in self._cores])

    # Container
    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]

    # Sized
    def __len__(self) -> int:
        return len(self._cores)

    # Subscriptable
    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._cores[item]
        if isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor


rgb = Paleta(Vermelho(), Verde(), Azul())

# Iterable
print("Iterable")
for cor in rgb:
    print(cor)
# Container
print("Container")
print("🟥" in rgb)
# Sized
print("Sized")
print(len(rgb))
# Subscriptable
print("Subscriptable")
print(rgb[0])
print(rgb["azul"])
