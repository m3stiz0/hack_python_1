"""
text: "FOOZIMAN" output => "fooziman"
"""

def fn_hack_2():
    result = "FOOZIMAN"
    #...
    return result.lower()

l = fn_hack_2()
print(l)