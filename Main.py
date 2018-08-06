from Robot import Robot
from Table import Table
from CommandInterpreter import CommandInterpreter as CmdInt

def main():
    table = Table(5, 5)
    robot = Robot(table)
    interpreter = CmdInt(robot)

    while(True):
        interpreter.execute(input("Enter command!\n"))


if(__name__ == "__main__"):
    main()