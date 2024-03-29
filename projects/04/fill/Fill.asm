// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

    @8192
    D=A 
    @range
    M=D             // range = 8192 (total # of SCREEN registers)

(LOOP)
    @SCREEN         // initialize variables start of every loop
    D=A
    @address
    M=D             // address = 16384 (screen's base memory address)

    @i
    M=0             // i = 0 (iteration variable)

    @KBD
    D=M
    @PRESSED
    D;JNE           // If (keyboard != 0) goto PRESSED
    @NOPRESS
    D;JEQ           // else goto NOPRESS

(NOPRESS)
    @range
    D=M
    @i      
    D=D-M           // D = range - i
    @LOOP
    D;JLT           // If (i > range) goto LOOP

    @address
    A=M
    M=0             // RAM[address] = 0 = 0000000000000000

    @i
    M=M+1           // i++
    @address
    M=M+1           // address++

    @KBD
    D=M
    @LOOP
    D;JNE       // If KBD != 0 goto LOOP

    @NOPRESS
    0;JMP           // goto NOPRESS


(PRESSED)
    @range
    D=M
    @i
    D=D-M           // D = range - i
    @LOOP
    D;JLT           // If (i > range) goto LOOP

    @address        // Set address to black
    A=M
    M=-1            // RAM[address] = -1 = 1111111111111111

    @i
    M=M+1           // i++
    @address
    M=M+1           // address++

    @KBD
    D=M
    @LOOP
    D;JEQ       // If KBD == 0 goto LOOP

    @PRESSED
    0;JMP           // goto PRESSED 


