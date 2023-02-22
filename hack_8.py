"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""



def fn_hack_8(object):
    result = []
    if len(object)%2:
        lenght = len(object)
        for item in object:
            lenght = lenght-1
            result.append( object[lenght]+"-"+str(object.index(object[lenght])+1))
        print(result)
    else:
        lenght = len(object)
        for item in object:
            lenght = lenght-1
            result.append(str(object.index(object[lenght])+1))
        print(result)
    return result

fn_hack_8(["a","b","c","d","e"])
fn_hack_8(["a","b","c"])
fn_hack_8(["a","b","c","d"])
fn_hack_8(["a","b"])