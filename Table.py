class Table:
    def __init__(self, width, height):
        if(width <= 0 or height <=0):
            print("Table dimensions not valid.")
        self.X = height
        self.Y = width

    def isOnTable(self, X, Y):
        return X <= self.X and Y <= self.Y and X >= 0 and Y >= 0