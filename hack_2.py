"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(word):

    result = ""

    for letter in word:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            result = result
        else:
            result = result + letter
    #...
    return result
