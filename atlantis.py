class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Engine:
    def __init__(self):
        self.active = True
        self.promptInput = ''
        self.commands = []
        self.startUpMessage = color.BOLD+color.CYAN+"Atlantis"+color.END+color.BOLD+" Portal initiated successfully ✅"+color.END
        self.endingMessage = color.BOLD+"Quitting "+color.CYAN+"Atlantis"+color.END+color.BOLD+" portal... "+color.END
        self.utils = self.Utils()
        self.preferences = self.Preferences
    def _commandInvokerNumberGenerator():
        i = 0
        while True:
            yield i
            i += 1

    _commandInvokerNumberGenObject = _commandInvokerNumberGenerator()
    def addCommand(self, command):
        invoker = next(self._commandInvokerNumberGenObject)
        command.update({"invoker": invoker})
        self.commands.append(command)
    def listCommands(self,headingText="COMMANDS MENU"):
        headingText = color.BOLD+headingText+color.END
        print("-"*80)
        print(f'{" "*((80//2)-(len(headingText)//2))}{headingText}')
        for i in self.commands:
            print(f'{" "*20}[{i["invoker"]}] -> {" "*3}{i["name"]}: {i["desc"]}')
        print("-"*80)
    def runCommand(self, cmdNumber):
        for i in self.commands:
            if cmdNumber == i["invoker"]: i["func"]()
    def setup(self):
        pass
    def loop(self,f=lambda: None):
        self._commandPrompt()
        f()
    def activatePortal(self):
        self.active = True
        print(self.startUpMessage)
        self.addCommand({"name": "help", "desc": "Lists all executable commands", "func": self.listCommands})
        try:
            
            self.setup()
            self.addCommand({"name": "quit", "desc": "Exit the portal", "func": self.deactivatePortal})
            if (self.preferences.RUN_HELP_ON_STARTUP):
                self.listCommands()
            while self.active == True:
                self.loop()
        except KeyboardInterrupt:
            self.deactivatePortal(q=False)
    
    def deactivatePortal(self,q=True):
        if q:
            r = self.utils.boolPrompt("Are you sure you want to quit?","y","n")
            if r:
                print("\n"+self.endingMessage)
                self.active = False
        else:
            print("\n"+self.endingMessage)
            self.active = False
    def _commandPrompt(self):
        try:
            cmd = int(self.utils.prompt("Execute Command:").strip())
            self.runCommand(cmd)
        except ValueError:
            print("Invalid command")
    class Utils:
        def __init__(self):
            pass
        def prompt(self,t,newline=False):
            t = color.BOLD+t+color.END+" "
            if newline:
                print(t)
                v = input()
            else :
                v = input(t)
            return v
        def boolPrompt(self,t,tt,ft):
            v = self.prompt(f"{t} [{tt}/{ft}]")
            if v.strip().casefold() == tt.strip().casefold(): return True
            elif v.strip().casefold() == ft.strip().casefold(): return False
            else: 
                print("Input invalid") 
                return False

    class Preferences:
        RUN_HELP_ON_STARTUP=True
