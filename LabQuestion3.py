p = True
q = True

def pTF(): return "T" if(p == True) else "F"
def qTF(): return "T" if(q == True) else "F"
def pANDq(): return "T" if(p and q) else "F"
def pORq(): return "T" if(p or q) else "F"
def pTHENq():  
    if(q):
        return "T"
    elif(p == q):
        return "T"
    else:
        return "F"
def pONLYq(): return "T" if(p == q) else "F"

print("<---------------------------------->")
print("<  p  q  |  p^q  pvq  p->q  p<->q  >")
print("<---------------------------------->")
print("<  " + pTF() + "  " + qTF() + "  |   " + pANDq() + "    " + pORq() + "    " + pTHENq() + "      " + pONLYq() + "    >")
q = False
print("<  " + pTF() + "  " + qTF() + "  |   " + pANDq() + "    " + pORq() + "    " + pTHENq() + "      " + pONLYq() + "    >")
p = False
q = True
print("<  " + pTF() + "  " + qTF() + "  |   " + pANDq() + "    " + pORq() + "    " + pTHENq() + "      " + pONLYq() + "    >")
q = False
print("<  " + pTF() + "  " + qTF() + "  |   " + pANDq() + "    " + pORq() + "    " + pTHENq() + "      " + pONLYq() + "    >")
print("<---------------------------------->")