"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(word):
    result = ""

    for letter in word:
        if letter == "f" or letter == "n" or letter == "b":
            result = result
        else:
            result = result + letter  
    #...
    return result