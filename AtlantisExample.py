import atlantis
portalEngine = atlantis.Engine()
userString = ""
def updateString():
    global userString
    userString = portalEngine.utils.prompt("Enter a string",newline=True)
def setupEngine():
    updateString()
    portalEngine.addCommand(
         {
         "name": "Reverse",
         "desc":"Reverse your string",
         "func":  lambda: print(userString[::-1])
          },
         )

    portalEngine.addCommand(
         {
         "name": "Length",
         "desc":"Get the length of the string",
         "func":  lambda: print(len(userString)),
          },
         )
    
    portalEngine.addCommand(
        {
        "name": "Verifiy Palindrome",
        "desc":"Verifies if the string is a palindrome",
        "func": lambda: print(userString == userString[::-1])
        }
    )
    portalEngine.addCommand(
        {
        "name": "Update String",
        "desc":"Change input string to a new string",
        "func": updateString
        }
    )

portalEngine.setup= setupEngine
portalEngine.activatePortal()
