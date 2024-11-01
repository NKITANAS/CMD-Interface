# THIS IS THE COMMAND PROMPT.
# This is where commands are executed and the CLI is shown


# Import Modules #

import commands


# Variables #

cmd_version = "0.0.1-alpha-dev"


# Functions #

# version Command - the ONLY command in interface
def version():
    return cmd_version


# Command Loop #

while True:
    cmd = input(">")