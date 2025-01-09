#1 feladat
n={3, 14, 18, 32, 14, 23, 28, 27, 26, 40, 0}

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
    print("Nem, nem lett több ötös, mint egyes.")
    
    
#3 feladat
n = 10
t = [3, 37, 18, 38, 3, 3, 28, 27, 39, 40]
psz = []

for i in range(41):
    psz.append(0)

for p in t:
    psz[p]+=1

lp=0
max_db=0

for i in range(41):
    if psz[i]> max_db:
        max_db=psz[i]
        lp=i

print(f"A {lp} pont fordult elő benne legtöbbször.")

#4.feladat
n4={3, 14, 18, 32, 14, 23, 28, 27, 26, 40, 0}

if 0 in n4:
    print("Igen, volt olyan diák, aki a nevén kívül nem írt rá semmit.")
else:
    print("nincs olyan diák")    
    
#vege