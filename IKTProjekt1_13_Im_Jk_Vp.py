#1 feladat
n={3, 14, 18, 32, 14, 23, 28, 27, 26, 40}

j=0

for i in n:
    if(i>20):
        j+=5
print(f"{j:.0f}% lett jobb mint 3-as")
    




#2 feladat
 
n = 10
t = [3, 37, 18, 38, 14, 23, 28, 27, 39, 40]  

otos = 0
egyes = 0


for i in t:
    if i >= 34:  
        otos += 1
    elif i < 12:  
        egyes += 1
if otos > egyes:
    print("Igen, több ötös lett, mint egyes.")
else:
    print("Nem, nem több ötös lett, mint egyes.")
    