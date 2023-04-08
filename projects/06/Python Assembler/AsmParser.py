# Parser module 
import re

class Parser:
                                        
    def __init__(self, file):                 # initializes parser by opening the file
        asm = open(file)                      # save the lines in a list (self.contents)

        self.contents = asm.readlines()
        self.parsed = []

        # Iterate thru contents list to simplify parse items
        for x in range(len(self.contents)):

            self.contents[x].replace('\n', '')              # remove new lines
            self.contents[x] = self.contents[x].strip()     # remove white space

            if self.contents[x].startswith('//'):           # skip comment lines
                continue

            if self.contents[x] == '':                      # skip empty fields 
                continue

            line_comment_split = self.contents[x].split('//')       # remove in-line comments
            self.contents[x] = line_comment_split[0]

            self.parsed.append(self.contents[x].strip())           # add qualified lines of code to list

        asm.close()
        
        

    def hasMoreCommands(self):                  # returns true if more lines left to parse
        return len(self.parsed) > 0
    


    def advance(self):                          # pops first item in list to advance parse
        if self.hasMoreCommands():
            self.parsed.pop(0)

    

    def commandType(self):                      # Determines command type based on pattern matches
        current_command = self.parsed[0]

        if current_command[0] == '@':            
            return 'A_COMMAND'
        
        elif re.match('\(.+\)', current_command):   
            return 'L_COMMAND'
        
        else: 
            return 'C_COMMAND'



    def symbol(self):                          # Returns symbol/decimal found in A or L commands
        if self.commandType() != 'C_COMMAND':
            symbol = self.parsed[0].strip('()@')
            return symbol
        


    def dest(self):                             # Returns 'dest' from C-command
        if self.commandType() == 'C_COMMAND':   
            command = self.parsed[0]

            # Split into before and after '=' sign
            equal_split = command.split('=')

            if len(equal_split) == 1:
                dest = None
            
            else: 
                dest = equal_split[0]
            
            return dest


    def comp(self):                            # Returns 'comp' from C-command
        if self.commandType() == 'C_COMMAND':
            command = self.parsed[0]

            # Split by semi-colon, remove dest mnemonic if present
            semicolon_split = command.split(';')

            equal_sign = semicolon_split[0].find('=')     # if '=' is present, return substring after equal sign
            if equal_sign != -1:
                comp = semicolon_split[0][(equal_sign + 1):]
            else:
                comp = semicolon_split[0]

            return comp
        

    def jump(self):
        if self.commandType() == 'C_COMMAND':
            command = self.parsed[0]

            colon_split = command.split(';')

            if len(colon_split) > 1:
                jump_command = colon_split[1]

            else:
                jump_command = None

            return jump_command