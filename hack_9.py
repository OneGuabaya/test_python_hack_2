"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(object):
    valor = ""
    result = {}
    
    for item in object:
        if item == "foo":
           for item_i in object[item]:
             if item_i != "k":
               valor = valor + item_i
               print(valor)
        result = {item.capitalize(): valor.capitalize()}
        return result