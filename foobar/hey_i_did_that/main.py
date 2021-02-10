def solution(n,b):
    k=len(n)
    zlist=[]
    while True:
        x = ''.join(sorted(n,reverse=True))
        y = ''.join(sorted(n))
        z10 = int(x,b) - int(y,b)
        if b!=10: n = toBaseN(z10,b)
        else: n=str(z10)
        if len(zlist)<k: n = n.zfill(k)
        if n in zlist: return len(zlist)-zlist.index(n)
        zlist.append(n)
        
def toBaseN(num,b):
    baseNnum=[]
    while num:
        baseNnum.insert(0,str(num%b))
        num=num//b
    return ''.join(baseNnum)