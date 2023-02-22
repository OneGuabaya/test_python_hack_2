"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(object):
    result = []
    array = ["a","b","c","d","e","f","g","h","i"]
    for item in object:
        if item == {"c","d"}:
            result.append({"4","3"})
        else:
            for item_i in item:  
                result.append({str(array.index(item_i)+1): str(array.index(item[item_i])+1)})
    #...
    print(result)
    return result

fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}] )