"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(array):
    result = []

    if array == []:
            result = ['0']
    else:
        for item in array:
            if array.index(item)%2:
                result.append("-")
            else:
                result.append(str(array.index(item)+1))
    #...
    return result