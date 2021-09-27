userspec=list(map(int,input("Enter chest size,waist size,hip size,shoulders length(in cm)").split()))
s=[30,28,30,40]
m=[32,30,34,42]
l=[34,32,36,43]
xl=[36,34,38,45]
diff=[]
diff.append((s[0]-userspec[0])+(s[1]-userspec[1])+(s[2]-userspec[2])+(s[3]-userspec[3]))
diff.append((m[0]-userspec[0])+(m[1]-userspec[1])+(m[2]-userspec[2])+(m[3]-userspec[3]))
diff.append((l[0]-userspec[0])+(l[1]-userspec[1])+(l[2]-userspec[2])+(l[3]-userspec[3]))
diff.append((xl[0]-userspec[0])+(xl[1]-userspec[1])+(xl[2]-userspec[2])+(xl[3]-userspec[3]))
temp=[]
for i in diff:
    if i>=0:
        temp.append(i)
key=diff.index(min(temp))        
if(key==0):
    print("S")
if(key==1):
    print("M")
if(key==2):
    print("L")
if(key==3):
    print("XL")
