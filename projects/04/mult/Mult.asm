// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

    @R0         // initialize variables
    D=M
    @x
    M=D         // x = R0 

    @R1
    D=M
    @y
    M=D         // y = R1

    @i
    M=0         // i = 0 (iteration variable of loop)

    @R2
    M=0         // product = 0

(LOOP)
    @y          // Check if loop should end or not
    D=M         // D = y
    @i
    D=D-M       // D = y - i
    @END
    D;JEQ       // If (i == y) goto END
            
    @x
    D=M            // Add x to product each iteration
    @R2
    M=D+M

    @i              // update i variable each iteration
    M=M+1
    @LOOP
    0;JMP           // Goto loop

(END)
    @END
    0;JMP       // Infinite loop