"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(word):
    result = ""

    for letter in word:
        if letter == "f":
            result = result + "F"
        elif letter == "o":
            result = result + "0"
        elif letter == "i":
            result = result + "¡"
        elif letter == "a":
            result = result + "@"
        elif letter == "n":
            result = result + "N"
        elif letter == "q":
            result = result + "Q"
        elif letter == "x":
            result = result + "X"
        elif letter == "u":
            result = result + "v"
        elif letter == "b":
            result = result + "B"
        else:
            result = result + letter

    #...
    return result