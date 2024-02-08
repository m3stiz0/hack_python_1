"""
text: "fooziman" output => "FOOZIMAN"
"""

def fn_hack_1():
    result = "fooziman"
    #...
    return result.upper()

u = fn_hack_1()
print(u)