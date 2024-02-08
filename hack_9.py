"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    total = len(result)
    resultLst = []
    i = 1

    while(i <= total ): 
        resultLst.append(i)
        resultLst.append('@')
        i+=1
    return resultLst

l = fn_hack_9()
print(l)