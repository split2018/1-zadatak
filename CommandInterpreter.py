class CommandInterpreter:
    def __init__(self, robot):
        self.robot = robot
        self.directions = ["north", "south", "east", "west"]

    def execute(self, command):
        commands = command.split(" ")
        if(self.robot.placed == False and commands[0].lower() != "place"):
            print("Robot must be placed on table!")
        else:
            for i in range(0, len(commands)):
                if(commands[i].lower() == "place"):
                    if(i<len(commands)-1):
                        pos = commands[i+1].split(',')
                    else:
                        print("Invalid command!\n")
                        return
                    if(pos[0].isdigit() and pos[1].isdigit() and pos[2].lower() in self.directions):
                        self.robot.placeOnTable(int(pos[0]), int(pos[1]), pos[2].upper())
                    else:
                        print("Invalid command!\n")

                if(commands[i].lower() == "report"):
                    self.robot.report()

                if(commands[i].lower() == "move"):
                    self.robot.move()

                if (commands[i].lower() == "left"):
                    self.robot.left()

                if (commands[i].lower() == "right"):
                    self.robot.right()
