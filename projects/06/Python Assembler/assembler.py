# Assembler module
import sys
from code import Code
from AsmParser import Parser


class Assembler:

    def __init__(self, file):       # Save file path and root name
        self.file = file
        self.filename = self.file.split('/')[-1].split('.')[0]


    def write_hack(self):
        output = open(f'{self.filename}.hack', 'w')         # 'w'rite mode overwrites the file each time it is writtent o

        parser_file = Parser(self.file)             # instantiate parser obj

        while parser_file.hasMoreCommands():                # while there are more lines to parse, translate current line and write to output hack file
            current_command = parser_file.parsed[0]

            if parser_file.commandType() == 'A_COMMAND':
                hack_code = self.getACommand(current_command)

            elif parser_file.commandType() == 'C_COMMAND':
                dest = parser_file.dest()
                comp = parser_file.comp()
                jump = parser_file.jump()

                hack_code = self.getCCommand(dest, comp, jump)


            output.write(f'{hack_code}\n')
            parser_file.advance()
            
        output.close()


    def getACommand(self, command):             # Convert A command to binary string
        decimal = command.replace('@', '')
        a_code = f'0{get_binary(int(decimal))}'

        return a_code
    

    def getCCommand(self, dest, comp, jump):
        dest_binary = Code.dest_code(dest)
        comp_binary = Code.comp_code(comp)
        jump_binary = Code.jump_code(jump)

        concat_binary = f'111{comp_binary}{dest_binary}{jump_binary}'

        return concat_binary



# Converts a decimal integer into 15-bit binary string
def get_binary(n):
    binary = ''
    i = 14

    while i >= 0:
        if 2**i > n:
            binary += '0'
            i -= 1
        else:
            binary += '1'
            n -= 2**i
            i -= 1

    return binary



def main():
    hack_file = Assembler(sys.argv[1])
    hack_file.write_hack()


if __name__ == "__main__":
    main()