import random

def isSubset(x, y):
    return True if(all(i in x for i in y)) else False

for i in range(0, 5):
    alist = []
    blist = []
    for i in range(0,5):
        n = random.randint(1, 10)
        m = random.randint(1, 10)
        alist.append(n)
        blist.append(m)
    print("<----------------------------------------------->")
    print("List A: " + str(alist))
    print("List B: " + str(blist))

    print("Union: ")
    clist = alist + blist
    print(clist)
    print()

    print("Intersection: ")
    clist = [i for i in alist if i in blist]
    print(clist)
    print()

    print("Difference of List A and List B: ")
    ablist = list(set(alist) - set(blist))
    print(ablist)
    print()

    print("Symmetric Difference of List A and List B: ")
    balist = list(set(blist) - set(alist))
    clist = ablist + balist
    print(clist)
    print()

    print("Is List A a Subset of List B: ")
    print(isSubset(alist, blist))
