"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    #...
    return result[0:7] + result[7].upper() 

u = fn_hack_4()
print(u)