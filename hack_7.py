"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""

def fn_hack_7(array):
    result = []

    if array == [0]:
        result = [0]
    else:
        for item in array:
            if array.index(item) == 0 or array.index(item)%3 and array.index(item) != 1:
             result.append(str(array.index(item)+1))
            else:
             result.append(array.index(item)+1)
            
    #...
    return result
    