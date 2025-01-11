# THIS IS THE COMMAND SCRIPT.
# This is the script where you would put commands that can be executed by the CLI.
# To put in a command, add it as another function. Then, put the function as though you are
# executing it in code in defs.txt (ex: If I have a function example() I would append 'example()' into defs.txt),
# put the command as you want it to be written into cmds.txt IN THE SAME LOCATION RELATIVE TO OTHER COMMANDS AS IT IS IN DEFS
# so if I have command example() I would put 'example' into cmds.txt and optionally add a description of the command in help.txt.


# Variables #

cmd_version = '0.0.1-alpha-dev'


# Functions #

# Printsntring function - in CLI: 'print <"string">' returns string
def printString(string):
    return string

# Version Command - gets the current version
def version():
    return cmd_version

