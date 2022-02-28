import pandas as pd

print('\nApplied Statistics - Discrete Variables\n')
print('Press "q" to stop insertion.\n')

title = input("• Please, insert your table title: ").upper()
data_type = input("• What kind of data are you working with? ")
source = input("• Tell us your source: ")
print("\n")

data = []
while True:
    try:
        d = input("- Insert a integer: ")
        if d == "q":
            break
        if d == "0" or int(d):
            data.append(d)
    except:
        print("• Sorry! It's not a integer. Try again")
          
print("\n",title)

rol = sorted(data)
elements = []
rows = []

for el in rol:
    count = 0
    
    if el not in elements:
        elements.append(el)
        rows.append([el, 1])
    else:
        for d in rows:
            if d[0] == el:
                d[1] = d[1] + 1    
        
Σfi = len(rol)  
Σfri = 0  

for idx, el in enumerate(rows):
    n = 0
    if idx == 0:
        rows[idx].append(el[1])
        rows[idx].append(round(el[1] / Σfi, 4))
        rows[idx].append(round(el[2] / Σfi, 4))
        Σfri += el[3]
    else:
        rows[idx].append(rows[idx-1][2] + rows[idx][1])
        rows[idx].append(round(el[1] / Σfi, 4))
        rows[idx].append(round(el[2] / Σfi, 4))
        Σfri += el[3]
        
i = 1
for r in rows:
    r.insert(0, i)
    i += 1
    
df = pd.DataFrame(data = rows, columns = ["i", data_type, "fi", "Fi", "fri", "Fri"]) 

print("\n")
print(df.to_string(index=False))
print(f'\nΣfi = {Σfi}')
print('\nΣfri =', round(Σfri, 4), "\n")
print("\nSource:",source)
print("\n")

