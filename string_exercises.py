# 1
string1 = input("Enter a string. ")
print(string1.upper())
print()

# 2
string2 = input("Enter a string. ")
print(string2.capitalize())
print()

# 3
string3 = input("Enter a string. ")
print(string3[::-1])
print()

# 4
string4 = input("Enter a paragraph to be translated to leetspeak. ")
string4upper = string4.upper()   
string4upper = string4upper.replace("A", "4")    
string4upper = string4upper.replace("E", "3")
string4upper = string4upper.replace("G", "6")
string4upper = string4upper.replace("L", "1")
string4upper = string4upper.replace("O", "0")
string4upper = string4upper.replace("S", "5")
string4upper = string4upper.replace("T", "7")
print(string4upper)
print()

# 5
string5 = input('Enter a word with a long vowel. ')
# string5 = list(string5)
# for char in string5:
#     print(char)
#     if string5[char:char + 1] == 'oo':
#         #string5 = string5.replace(char, char*4)
#         print(string5)
#         # print(string5[:char - 1] + (string5[char] * 5) + string5[char + 1:])
string5 = string5.replace("oo", "ooooo")
string5 = string5.replace("aa", "aaaaa")
string5 = string5.replace("ee", "eeeee")
string5 = string5.replace("ii", "iiiii")
string5 = string5.replace("uu", "uuuuu")
print(string5) 
print()

# 6
string6 = input("Enter a string. ")
string6 = string6.lower()
empty_string6 = ""
for char in string6:
    if char == "a":
        string6 = string6.replace("a", "n")
        empty_string6 = empty_string6 + "n"
    elif char == "b":
        string6 = string6.replace("b", "o")
        empty_string6 = empty_string6 + "o"
    elif char == "c":
        string6 = string6.replace("c", "p")
        empty_string6 = empty_string6 + "p"
    elif char == "d":
        string6 = string6.replace("d", "q")
        empty_string6 = empty_string6 + "q"
    elif char == "e":
        string6 = string6.replace("e", "r")
        empty_string6 = empty_string6 + "r"
    elif char == "f":
        string6 = string6.replace("f", "s")
        empty_string6 = empty_string6 + "s"
    elif char == "g":
        string6 = string6.replace("g", "t")
        empty_string6 = empty_string6 + "t"
    elif char == "h":
        string6 = string6.replace("h", "u")
        empty_string6 = empty_string6 + "u"
    elif char == "i":
        string6 = string6.replace("i", "v")
        empty_string6 = empty_string6 + "v"
    elif char == "j":
        string6 = string6.replace("j", "w")
        empty_string6 = empty_string6 + "w"
    elif char == "k":
        string6 = string6.replace("k", "x")
        empty_string6 = empty_string6 + "x"
    elif char == "l":
        string6 = string6.replace("l", "y")
        empty_string6 = empty_string6 + "y"
    elif char == "m":
        string6 = string6.replace("m", "z")
        empty_string6 = empty_string6 + "z"
    elif char == "n":
        string6 = string6.replace("n", "a")
        empty_string6 = empty_string6 + "a"
    elif char == "o":
        string6 = string6.replace("o", "b")
        empty_string6 = empty_string6 + "b"
    elif char == "p":
        string6 = string6.replace("p", "c")
        empty_string6 = empty_string6 + "c"
    elif char == "q":
        string6 = string6.replace("q", "d")
        empty_string6 = empty_string6 + "d"
    elif char == "r":
        string6 = string6.replace("r", "e")
        empty_string6 = empty_string6 + "e"
    elif char == "s":
        string6 = string6.replace("s", "f")
        empty_string6 = empty_string6 + "f"
    elif char == "t":
        string6 = string6.replace("t", "g")
        empty_string6 = empty_string6 + "g"
    elif char == "u":
        string6 = string6.replace("u", "h")
        empty_string6 = empty_string6 + "h"
    elif char == "v":
        string6 = string6.replace("v", "i")
        empty_string6 = empty_string6 + "i"
    elif char == "w":
        string6 = string6.replace("w", "j")
        empty_string6 = empty_string6 + "j"
    elif char == "x":
        string6 = string6.replace("x", "k")
        empty_string6 = empty_string6 + "k"
    elif char == "y":
        string6 = string6.replace("y", "l")
        empty_string6 = empty_string6 + "l"
    elif char == "z":
        string6 = string6.replace("z", "m")
        empty_string6 = empty_string6 + "m"
    elif char == " ":
        empty_string6 = empty_string6 + " "
print(empty_string6)


    