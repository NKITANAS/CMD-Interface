# CMD Interface
CMD interface is a pre-built command CLI for python projects. 
* NOT CURRENTLY IN WORkING CONDITION.
## Adding a Command
To add a command there are 3 steps.
* Step 1: Write what the command does in a function in commands.py
* Step 2: Put the function into functions.txt as though you are writing it in code in interface.py, with other functions seperated by a '>'. Example functions.txt: commands.function1(a, b, c)>commands.function2()>commands.yourfunction(a, b)
* Note: Although you can name your variables in any way you want while defining the function, variables must be named in alphabetical order using letters 'a', 'b', 'c', etc. in the defenitions.txt file.
* Step 3: In the same spot as you wrote the function in functions.txt, write the corresponding command you want to be assigned to the function in commands.txt with NO VARIABLES. Example commands.txt: functioncommand1>functioncommand2>yourcommand
Aand youve added a command! This way, you can add many commands without having to write an if statement over and over again.
## This is fun and all, but how does this work?
Simple! It is done by importing and splitting the text files, putting all of them into seperate lists, and checking the new 'commands' list for a match with the input given. Then, the command is split into vars and variables are assined. Then the exec() function is used to execute the function from a string.
