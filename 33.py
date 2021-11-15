Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> age = 64
retirement = age - 65

if retirement < 10:
    print("Пора на пенсию, дружок!")
else:
    print("Дружище, тебе еще рано думать о пенсии!")
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
age = 6
retirement = age - 65

if retirement < 10:
    print("Пора на пенсию, дружок!")
else:
    print("Дружище, тебе еще рано думать о пенсии!")