import itertools as it
def f():
    LL=[]
    L=[1,2,3,4,5,6,7,8,9]
    L1=list(it.permutations(L,2))
    for t1 in L1:
        p=t1[0]*10+t1[1]
        Li=[i for i in L if i not in t1]
        L2=list(it.permutations(Li,3))
        for t2 in L2:
            q=t2[0]*100+t2[1]*10+t2[2]
            Lii=[i for i in Li if i not in t2]
            L3=list(it.permutations(Lii,4))
            for t3 in L3:
                n=t3[0]*1000+t3[1]*100+t3[2]*10+t3[3]
                if n==p*q: LL.append([p,q,n])
    return LL
