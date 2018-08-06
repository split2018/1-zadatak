class Robot:
    def __init__(self, table):
        self.placed = False
        self.table = table

    def placeOnTable(self, X, Y, facing):
        if(self.table.isOnTable(X,Y)):
            self.X = X
            self.Y = Y
            self.facing = facing
            self.placed = True
            return
        print("Robot not placed on table!")

    def report(self):
        print("(" + str(self.X) + ", " + str(self.Y) + "), " + self.facing)

    def move(self):
        if(self.facing.lower() == "north" and self.table.isOnTable(self.X, self.Y + 1)):
            self.Y += 1


        elif (self.facing.lower() == "south" and self.table.isOnTable(self.X, self.Y - 1)):
            self.Y -= 1


        elif (self.facing.lower() == "south" and self.table.isOnTable(self.X - 1, self.Y)):
            self.X -= 1


        elif (self.facing.lower() == "east" and self.table.isOnTable(self.X + 1, self.Y)):
            self.X += 1

        else:
            print("Can't move robot")

    def left(self):
        if(self.facing.lower() == "north"):
            self.facing = "WEST"

        elif (self.facing.lower() == "west"):
            self.facing = "SOUTH"

        elif (self.facing.lower() == "south"):
            self.facing = "EAST"

        elif (self.facing.lower() == "east"):
            self.facing = "NORTH"

    def right(self):
        if (self.facing.lower() == "north"):
            self.facing = "EAST"

        elif (self.facing.lower() == "east"):
            self.facing = "SOUTH"

        elif (self.facing.lower() == "south"):
            self.facing = "WEST"

        elif (self.facing.lower() == "west"):
            self.facing = "NORTH"