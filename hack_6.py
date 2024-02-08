"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    i = 0
    result = [0,1,2,3,4,5]

    for i in result:    
        return result  
p = fn_hack_6()
print(p)