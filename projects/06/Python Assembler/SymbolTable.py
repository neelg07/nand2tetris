# Symbol Table Module
# Handles all occurences of symbols in variables and/or labels

class SymbolTable:
    def __init__(self):
        self.symbols = {}


    def addEntry(self, symbol, address):
        self.symbols[symbol] = address


    def contains(self, symbol):
        return symbol in self.symbols.keys()
    

    def getAddress(self, symbol):
        if self.contains(symbol):
            return self.symbols[symbol]
