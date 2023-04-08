# Code module

class Code:

    comp_table_0 = {
        '0': '101010',
        '1': '111111',
        '-1': '111010',
        'D': '001100',
        'A': '110000',
        '!D': '001101',
        '!A': '110001',
        '-D': '001111',
        '-A': '110011',
        'D+1': '011111',
        'A+1': '110111',
        'D-1': '001110',
        'A-1': '110010',
        'D+A': '000010',
        'D-A': '010011',
        'A-D': '000111',
        'D&A': '000000',
        'D|A': '010101'
    }

    comp_table_1 = {
        'M': '110000',
        '!M': '110001',
        '-M': '110011',
        'M+1': '110111',
        'M-1': '110010',
        'D+M': '000010',
        'D-M': '010011',
        'M-D': '000111',
        'D&M': '000000',
        'D|M': '010101'
    }

    jump_table = {
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }
    
    @classmethod
    def dest_code(cls, dest_mnemonic):          # Dest conversion method
        code = ''

        if dest_mnemonic == None:
            return '000'
        
        if 'A' in dest_mnemonic:      # A code -> 'X00'
            code += '1'
        else: 
            code += '0'

        if 'D' in dest_mnemonic:      # D code -> '0X0'
            code += '1'
        else:
            code += '0'

        if 'M' in dest_mnemonic:       # M code -> '00X'
            code += '1'
        else:
            code += '0'

        return code
    


    @classmethod
    def comp_code(cls, comp_mnemonic):          # Comp conversion method
        
        if 'M' in comp_mnemonic:                                # a = 1
            code = '1' + Code.comp_table_1[comp_mnemonic]
        
        else:
            code = '0' + Code.comp_table_0[comp_mnemonic]         # a = 0

        return code
    


    @classmethod
    def jump_code(cls, jump_mnemonic):          # Jump conversion method

        if jump_mnemonic == None:
            return '000'
        else:
            return Code.jump_table[jump_mnemonic]