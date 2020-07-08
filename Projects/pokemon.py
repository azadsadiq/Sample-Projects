class Pokemon:
  def __init__(self, name, type, level = 5):
    self.name = name
    self.level = level
    self.type = type
    self.health = level * 5
    self.max_health = level * 5
    self.is_knocked_out = False
  
  def __repr__(self):
    return f"This level {self.level} {self.name} has {self.health} hit points remaining. They are a {self.type} type Pokemon"

  def revive(self):
    self.is_knocked_out = False
    if self.health == 0:
      self.health = 1
    print(f"{self.name} was revived!")

  def knock_out(self):
    self.is_knocked_out = True
    if self.health != 0:
      self.health = 0
    print(f"{self.name} was knocked out!")

  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.knock_out()
    else:
      print(f"{self.name} now has {self.health} health.")

  
  def gain_health(self, amount):
    if self.health == 0:
      self.revive()
    self.health += amount
    if self.health >= self.max_health:
      self.health = self.max_health
    print(f"{self.name} now has {self.health} health.")

  def attack(self, other_pokemon):
    if self.is_knocked_out:
      print(f"{self.name} can't attack because it is knocked out.")
    return
    if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
      print(f"{self.name} attacked other_pokemon.name for ({self.level} * 0.5) damage")
      print(f"It's not very effective")
      other_pokemon.lose_health(round(self.level * 0.5))
# If the pokemon attacking has neither advantage or disadvantage, then it deals damage equal to its level to the other pokemon
    if (self.type == other_pokemon.type):
      print(f"{self.name} attacked other_pokemon.name for {self.level} damage.")
      other_pokemon.lose_health(self.level)
# If the pokemon attacking has advantage, then it deals damage equal to double its level to the other pokemon
    if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
      print(f"{self.name} attacked other_pokemon.name for ({self.level} * 2) damage.")
      print("It's super effective")
      other_pokemon.lose_health(self.level * 2)

#Three classes that are subclasses of Pokemon
class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)

#trainer class
class Trainer:
  def __init__(self, pokemon_list, num_potions, name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name
    
  def __repr__(self):
        # Prints the name of the trainer, the pokemon they currently have, and the current active pokemon.
        print(f"The trainer {self.name} has the following pokemon")
        for pokemon in self.pokemons:
            print(pokemon)
        print(pokemon)
        return "The current active pokemon is {name}".format(name = self.pokemons[self.current_pokemon].name)

  def switch_active_pokemon(self, new_active):
    # Switches the active pokemon to the number given as a parameter
    # First checks to see the number is valid (between 0 and the length of the list)
        if new_active < len(self.pokemons) and new_active >= 0:
          # You can't switch to a pokemon that is knocked out
          if self.pokemons[new_active].is_knocked_out:
            print(f"{self.pokemons[new_active].name} is knocked out. You can't make it your active pokemon")
            # You can't switch to your current pokemon
          elif new_active == self.current_pokemon:
            print(f"{self.pokemons[new_active].name} is already your active pokemon")
            # Switches the pokemon
          else:
                self.current_pokemon = new_active
                print(f"Go {self.pokemons[self.current_pokemon].name}, it's your turn!")

  def use_potion(self):
        # Uses a potion on the active pokemon, assuming you have at least one potion.
        if self.potions > 0:
            print("You used a potion on {name}.".format(name = self.pokemons[self.current_pokemon].name))
            # A potion restores 20 health
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("You don't have any more potions")

  def attack_other_trainer(self, other_trainer):
        # Your current pokemon attacks the other trainer's current pokemon
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)

# Six pokemon are made with different levels. (If no level is given, it is level 5)
a = Charmander(7)
b = Squirtle()
c = Squirtle(1)
d = Bulbasaur(10)
e = Charmander()
f = Squirtle(2)

#Two trainers are created. The first three pokemon are given to trainer 1, the second three are given to trainer 2.
trainer_one = Trainer([a,b,c], 3, "Alex")
trainer_two = Trainer([d,e,f], 5, "Sara")

print(trainer_one)
print(trainer_two)

# Testing attacking, giving potions, and switching pokemon.
trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)
trainer_two.use_potion()
trainer_one.attack_other_trainer(trainer_two)
trainer_two.switch_active_pokemon(0)
trainer_two.switch_active_pokemon(1)


