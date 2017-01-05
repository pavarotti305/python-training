# Parent class Things
class Things:
    pass


# Child class Inanimates of parent Things
class Inanimates(Things):
    pass


# Child class Animates of parent Things
class Animates(Things):
    pass


# Child class SideWalk of parent Inanimates
class SideWalk(Inanimates):
    pass


# Child class Animals of parent Animates
class Animals(Animates):
    def breathe(self):
        print("breathe")

    def move(self):
        print("move")

    def eat(self):
        print("eat")


# Child class Mammals of parent Animals
class Mammals(Animals):
    def feed_their_sweet_with_milk(self):
        print("feed sweet")


# Child class Giraffe of parent Mammals
class Giraffe(Mammals):
    def eat_the_leaves_of_the_trees(self):
        print("eat the leaves")

# Advantage of class we can use functions of all other class by using self.function we want to use
    def find_food(self):
        self.move()
        print("I have found food and now I can")
        self.eat()

regine = Giraffe()
melman = Giraffe()
regine.find_food()