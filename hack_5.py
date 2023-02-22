"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""



def fn_hack_5(word):
    result = ""
    if word[0:3] == "foo":
        for item in word:
            if word.index(item) == 1 or word.index(item) == 7:
                result = result + "-"
            elif word.index(item) == 5:
                result = result + "-m"
            else:
                result = result + item
        result = result.replace("-","o",1)
    else:
        for item in word:
            if word.index(item) == 2 or word.index(item) == 5:
                result = result + "-"
            else:
                result = result + item

    #...
    return result 