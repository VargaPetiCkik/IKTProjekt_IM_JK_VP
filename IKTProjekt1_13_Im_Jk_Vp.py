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
    print("Nem, nem lett több ötös, mint egyes.")
    
#3 feladat

n = 10
t = [3, 37, 18, 38, 3, 3, 28, 27, 39, 40]

pontok_szama = {}

for pont in t:
    if pont in pontok_szama:
        pontok_szama[pont] += 1
    else:
        pontok_szama[pont] = 1

l= None
max_db = 0

for pont, db in pontok_szama.items():
    if db > max_db:
        max_db = db
        l = pont

print(f"A {l} pont fordult elő benne legtöbbször.")

#4.feladat