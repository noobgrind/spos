IS = {
    "STOP" : "00",
    "ADD" : "01",
    "SUB" : "02",
    "MULT" : "03",
    "MOVER" : "04",
    "MOVEM" : "05",
    "COMP" : "06",
    "BC" : "07",
    "DIV" : "08",
    "READ" : "09",
    "PRINT" : "10"
    }

DL = {"DC" : "01",
      "DS" : "02"}
AD = {
    "START" : "01",
    "END" : "02",
    "ORIGIN" : "03",
    "EQU" : "04",
    "LTORG" : "05"
    }
REG = {
    "AREG" : "01",
    "BREG" : "02",
    "CREG" : "03",
    "DREG" : "04"
    }
COND = {
    "LT" : "1",
    "LE" : "2",
    "EQ" : "3",
    "GT" : "4",
    "GE" : "5",
    "ANY" : "6"
    }

#Symbol Table - 
f1 = open("Sym_tab.txt",'r')
s = f1.read()
s = s.splitlines()
sym_tab = {}
for i in s:
    m = i.split()
    sym_tab[m[0]] = m[2]

#Literal Table -
f2 = open("Lit_tab.txt",'r')
l = f2.read()
l = l.splitlines()
lit_tab = {}
for i in l:
    m = i.split()
    lit_tab[m[0]] = m[2]


#Intermediate Code -
f = open('IC.txt','r')
data = f.read()
data = data.replace("(","")
data = data.replace(")","")
# data = data.replace(","," ")
data = data.splitlines()

for i in data:
    m = i.split()
    print(m)

for i in data:
    m = i.split()
    
 
#     print((m[1].split(',')) if len(m) > 1 else "")
#     print(m)
    if m[0].isnumeric():
        print(f"{m[0]})  +", end=' ')
    else:
        print()
    
    if len(m) > 2 and len(m[1]) > 3 and m[1][1] == 'L' and m[1][-1] == '1':
        n = m[2].split(',')
        print(f"00  0  {int(n[1]):03}", end = "\n")
    
#     if (len(m) > 2 and len(m[1]) > 3 and m[1][1] == 'L' and m[1][-1] == '2'):
#         print("\b\b\b   ") 
    
    
    if len(m) > 1 and m[1][0] == 'I':
        n = m[1].split(',')
        print(n[1] , end = "  ")
        if int(n[1]) == 0:
            print("0  000")
        
    if len(m) > 2 and m[2][0] == 'R':
        n = m[2].split(',')
        n = int(n[1])
        print(f"{n}  " , end ="" )
    elif len(m) > 2 and m[2][0] != 'R' and m[1][0] != 'D':
        
        if m[2].isnumeric():
            print(f"{m[2]}  " ,end = "")
        else:
            print("0   ",end="")
            
    if len(m) > 3 and (m[3][0] == 'S' or m[3][0] == 'L'):
        n = m[3].split(',')
        if m[3][0] == 'L':
            print(lit_tab[n[1]])
        else:
            print(sym_tab[n[1]])
#     print()
            

f.close()
f1.close()
f2.close()

