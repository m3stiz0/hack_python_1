"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    ls1 = []
    ls2 = []
    result = "fooziman"
    ls2.append(result.replace("fooziman", "F00Z1M@N"))
    ls1 = list(ls2[0])
    return ls1  

k = fn_hack_10()
print(k)