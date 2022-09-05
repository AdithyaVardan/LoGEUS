def AND(x,y):
    if (x==1)&(y==1):
        return 1
    else:
        return 0
def OR(x,y):
    if (x==1)|(y==1):
        return 1
    else:
        return 0
def NOT(x):
    if(x==1):
        return 0
    else:
        return 1
def NOR(x,y):
    return NOT(OR(x,y))
def NAND(x,y):
    return NOT(AND(x,y))
def XOR(x,y):
    if (x==0&y==0)|(x==1&y==1):
        return 0
    else:
        return 1
def XNOR(x,y):
    return NOT(XOR(x,y))
def tt():
    print("A     B     A      x'     Y'     O      A'     XO     O'     XO'")
    for i in range(0,2):
        for j in range(0,2):
            print(i,"   ",j,"   ",AND(i,j),"    ",NOT(i),"    ",
                    NOT(j),"    ",OR(i,j),"    ",NAND(i,j)
                    ,"    ",XOR(i,j),"    ",NOR(i,j),"    ",XNOR(i,j))
