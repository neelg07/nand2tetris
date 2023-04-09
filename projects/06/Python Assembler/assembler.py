# Assembler module
import sys
from code import Code
from AsmParser import Parser
from SymbolTable import SymbolTable

class Assembler:

    def __init__(self, file):       # Save file path and root name
        self.file = file
        self.filename = self.file.split('/')[-1].split('.')[0]
        self.var_count = 16


    def write_hack(self, symbol_table):

        output = open(f'{self.filename}.hack', 'w')         # 'w'rite mode overwrites the file each time it is writtent o

        parser_file = Parser(self.file)             # instantiate parser obj

        while parser_file.hasMoreCommands():                # while there are more lines to parse, translate current line and write to output hack file

            if parser_file.commandType() == 'A_COMMAND':
                symbol = parser_file.symbol()
                hack_code = self.getACommand(symbol, symbol_table)

            elif parser_file.commandType() == 'C_COMMAND':
                dest = parser_file.dest()
                comp = parser_file.comp()
                jump = parser_file.jump()

                hack_code = self.getCCommand(dest, comp, jump)

            else:
                parser_file.advance()
                continue


            output.write(f'{hack_code}\n')
            parser_file.advance()
            
        output.close()


    def getACommand(self, symbol, symbol_table):                  
        if symbol.isdigit():                            # Convert A command to binary string if digit
            a_code = f'0{get_binary(int(symbol))}'      # or get saved value from symbol table
        
        elif symbol in symbol_table.keys():
            address = symbol_table[symbol]
            a_code = f'0{get_binary(address)}'

        else:
            symbol_table.addEntry(symbol, self.var_count)
            self.var_count += 1
            
            address = symbol_table[symbol]
            a_code = f'0{get_binary(address)}'

        return a_code
    

    def getCCommand(self, dest, comp, jump):
        dest_binary = Code.dest_code(dest)
        comp_binary = Code.comp_code(comp)
        jump_binary = Code.jump_code(jump)

        concat_binary = f'111{comp_binary}{dest_binary}{jump_binary}'

        return concat_binary
    

    def createSymbolTable(self):
        symbol_table = SymbolTable()
        first_parse = Parser(self.file)
        instruction = 0

        while first_parse.hasMoreCommands():                   # parse entire script, add L_Commands (symbol, ins. mem) into symbol table
            
            if first_parse.commandType() == 'L_COMMAND':
                symbol = first_parse.symbol()
                symbol_table.addEntry(symbol, instruction)
                first_parse.advance()

            else:
                instruction += 1
                first_parse.advance()

        return symbol_table.symbols




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
    table = hack_file.createSymbolTable()
    hack_file.write_hack(table)


if __name__ == "__main__":
    main()