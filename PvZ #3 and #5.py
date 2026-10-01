class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        if self.health > 0:
            print(f"{self.name} attacks {zombie.name} for {self.damage} damage.")
            zombie.take_damage(self.damage)
        else:
            print(f"{self.name} is defeated and cannot attack.")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Remaining health: {self.health}")

        if self.health <= 0:
            print(f"{self.name} has been defeated.")


class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        if self.distance > 0:
            self.distance -= 1
            print(f"{self.name} moves closer. Distance to plants: {self.distance}")
        else:
            print(f"{self.name} is at the plants and will attack.")

    def attack(self, plant):
        if self.health > 0 and self.distance == 0:
            print(f"{self.name} attacks {plant.name} for {self.damage} damage.")
            plant.take_damage(self.damage)
        else:
            print(f"{self.name} cannot attack yet.")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Remaining health: {self.health}")

        if self.health <= 0:
            print(f"{self.name} has been defeated.")



peashooter = Plant("Peashooter", 50, 10)
repeater = Plant("Repeater", 50, 15)


zombie = Zombie("Zombie", 150, 20, 2)

turn = 1

while True:
    print(f"\n--- TURN {turn} ---")

    \
    if peashooter.health > 0:
        peashooter.attack(zombie)

    
    if zombie.health <= 0:
        print("\nplants win!")
        break

    
    if repeater.health > 0:
        repeater.attack(zombie)

    
    if zombie.health <= 0:
        print("\nplants win!")
        break

    
    if zombie.distance > 0:
        zombie.move()
    else:
        
        if peashooter.health > 0:
            zombie.attack(peashooter)
        elif repeater.health > 0:
            zombie.attack(repeater)

   
    if peashooter.health <= 0 and repeater.health <= 0:
        print("\nzombie wins!")
        break

    
    print(f"Peashooter health: {peashooter.health}")
    print(f"Repeater health: {repeater.health}")
    print(f"Zombie health: {zombie.health}")
    print(f"Zombie distance: {zombie.distance}")

    turn += 1