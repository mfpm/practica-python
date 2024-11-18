class pokemon:
  def __init__(self, name, tipo):
    self.name= name
    self.tipo=tipo

  def description(self):
    return f"this Pokemon's name is {self.name} and it's type is {self.tipo}"

  def attack(self, attack):
    return f"{self.name} used {attack}... it's super effective"
  
starmie = pokemon("Starmie","water/psychic")

print(starmie.description())
a= input("Ingrese un ataque: ")
print(starmie.attack(a))
