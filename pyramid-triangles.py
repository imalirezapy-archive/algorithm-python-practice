# github: https://github.com/imalirezapy
# Hope you enjoy (:

x = int(input())

n = 1 + (3 * x) + x
bs = list(range(n-1, -1, -1)) # back space
cs = [] # center space
for i in range(x+1):
    cs.extend([0, 1, 3, 5])

ll = [] # last line stars
for i in range(1, x+1):
    n2 = 1 + (3 * i) + i
    ll.append((n2 * 2) - 1)


print(" " * bs[0] + "*")
c = 1
cl = 0
cl2 = 0
for i in range(1, n-1):
    if cl2 == 0:
        string = " " * bs[i]+"*" + " "*cs[c] + "*"
        sl = list(string)
        if cl > 0:
    
            if cs[c] == 1:
                sl.append((("     *") + " "*cs[c] + "*")*cl)
            elif cs[c] == 3:
                sl.append((("   *") + " "*cs[c] + "*")*cl)
            elif cs[c] == 5:
                sl.append(((" *") + " "*cs[c] + "*")*cl)
                
        print("".join(sl))
    elif cl > 0:
        cl2 -= 1   
    c += 1
    if cs[c] == 0:
        if ll[cl] == ll[0]:
            print(" "*bs[i+1] +ll[cl]*"*", end="")
        else:
            print(" " * (bs[i+1])+ ll[cl] *"*", end="")
        cl += 1
        cl2 += 1
        print()