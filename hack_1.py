"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""

def fn_hack_1(palabra):
    
    if 'o' in palabra and 'i' in palabra:
        if palabra.index('o') == 1:
            result = palabra.replace('o','O',palabra.index('o'))
            result = result.replace('i','I',result.index('i'))
            return result
    elif "u" in palabra:
        if palabra.index('u') == 1:
            result = palabra.replace('u','U',palabra.index('u'))
            return result
    else:
        result = palabra
        return result
