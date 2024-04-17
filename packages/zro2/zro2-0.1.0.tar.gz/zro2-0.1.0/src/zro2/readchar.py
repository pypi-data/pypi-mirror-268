import functools
import typing
import readchar as readchar

class CliSelection:
    def __init__(self, options : list, index=0):
        self.__options = options
        self.__index = index
        self.__dactionMarker = False
        self.clearScreenMethod : typing.Literal["clear", "movedown"] = "clear"
        self.printMethod = print
    @property
    def options(self):
        return list(self.__options)
    
    @property
    def selected(self):
        return self.__options[self.__index]

    def helpcommand(self):
        self.printMethod("Arrow keys/WASD and Enter to select.")

    def clearScreen(self):
        if self.clearScreenMethod == "clear":
            self.printMethod("\033[H\033[J")
        elif self.clearScreenMethod == "movedown":
            self.printMethod('\n' * 20)
            # focus on the current line
            self.printMethod("\x1b[1;1H")

    def run(self):
        self.helpcommand()
        while True:
            # Display options
            for i, option in enumerate(self.__options):
                prefix = "->" if i == self.__index else "  "
                self.printMethod(f"{prefix} {option}")

            if self.__dactionMarker:
                self.daction()
                self.__dactionMarker = False
            
            # Read key press
            key = readchar.readkey()

            # Up (W)
            if (key == 'w' or key == '\x00H') and self.__index > 0:
                self.__index -= 1
            # Down (S)
            elif (key == 's' or key == '\x00P') and self.__index < len(self.options) - 1:
                self.__index += 1
            elif (key == 'a' or key == '\x00K'):
                return -1
            elif (key == 'd' or key == '\x00M'):
                self.__dactionMarker = True

            # Enter to select
            elif key == readchar.key.ENTER:
                self.onComplete()
                break

            self.clearScreen()
        return 0
    
    def daction(self):
        pass

    @property
    def index(self):
        return self.__index

    def onComplete(self):
        self.printMethod(f"You selected: {self.options[self.__index]}")

