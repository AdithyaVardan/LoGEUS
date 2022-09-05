import gates
print("A     B     A      x'     Y'     O      A'     XO     O'     XO'")
for i in range(0,2):
    for j in range(0,2):
        print(i,"   ",j,"   ",gates.AND(i,j),"    ",gates.NOT(i),"    ",
                gates.NOT(j),"    ",gates.OR(i,j),"    ",gates.NAND(i,j)
                ,"    ",gates.XOR(i,j),"    ",gates.NOR(i,j),"    ",
                gates.XNOR(i,j))
