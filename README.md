# [From Nand to Tetris](https://www.nand2tetris.org/software)
Building a Modern Computer From First Principles


* Book: [The Elements of Computing Systems](https://mitpress.mit.edu/books/elements-computing-systems)
* Instructors: Shimon Schocken & Noam Nisan

## Overview
This project is from the MOOC course nand2tetris. From building basic elementary logic gates to writing a high level language and operating system, this course will teach me how to build a modern-day, all-purpose PC from the ground up.

By digging deep into the implementations behind the multi-layered abstractions used to create the hardware and software, I hope to reach a higher understanding behind the lower-level processes that make up today's computing world.

## Course Visual Roadmap

![roadmap](./images/roadmap.png)

## Projects

* Project 0: Introduction 
* [Project 1: Boolean Logic](#project-1)
* [Project 2: Boolean Arithmetic](#project-2)
* Project 3: Sequential Logic   
* Project 4: Machine Language 
* Project 5: Computer Architecture  
* Project 6: Assembler   
* Project 7: VM I: Stack Arithmetic   
* Project 8: VM II: Program Control   
* Project 9: High-Level Language  
* Project 10: Compiler I: Syntax Analysis   
* Project 11: Compiler II: Code Generation   
* Project 12: Operating System 

## Project 1
- Used logic and boolean algebra to reduce and simplify the implementation of several elementary logic gates. De Morgan's Laws and Distributive property were particularly useful.

- Started with only a Nand gate but used previously-built chips for chip implementations down the line to avoid redundancy and to simplify complexity.

- Played around with a logic gate simulator to determine inner chip gate links as problems got more complex.

- Implementation of Mux and DMux were the most difficult and required several different try, check, and revise cycles but eventually came to a solution that seems to be close to optimal, if not optimal. 

- Multi-bit elementary gates were the easiest to implement since it is just stacking an array of n elementary gates for an n-bit complex gate.

- Multi-way gates, or multi-input gates, were tricky at first, but easy enough once the pattern showing the relationship between an m-way gate and its normal elementary gate was found. 

## Project 2