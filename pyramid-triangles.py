# github: https://github.com/imalirezapy
# Hope you enjoy (:

n = int(input())
t = 5 # triangle size
m = lambda v: v*2*(t-1)+1
w, w1 = m(n), m(1)-4

for i in range(n):
    mi = m(i)
    sp = (w-mi)//2
    print(' '*sp+'*'*mi)
    for j in range(t-2):
        k, l = 2*j+1, w1-2*j
        s = '*'+' '*k+'*'+' '*l
        sp -= 1
        print(' '*sp+(s*(i+1))[:-l-1]+'*')
print('*'*w)