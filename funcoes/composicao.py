names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian",
]

# TODO: Usar lambdas
def starts_with_b(text):
    return text[0].lower() == "b"

print(*list(filter(starts_with_b, names)))