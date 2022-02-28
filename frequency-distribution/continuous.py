import pandas as pd
import math

print('\nApplied Statistics - Continuous Variables\n')
print('Press "q" to stop insertion.\n')

title = input("• Please, insert your table title: ").upper()
data_type = input("• What kind of data are you working with? ")
source = input("• Tell us your source: ")
print("\n")

# GETTING DATA
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

# INTEGERS ARRAY
int_data = [int(el) for el in data]

# ROL - SORTING DATA
rol = sorted(int_data)

# N
n = len(int_data)

# STRUGES RULE
i = round(4.3 * math.log(n, 10))

# AMPLITUDE
max = max(int_data)
min = min(int_data)
h = round((max - min) / i)

# GENERATE COLUMN 
rows = []
tmp = min
idx = 1
while True:
    if tmp < max:
        rows.append([idx, [tmp, tmp+h], 0])
        tmp += h
    else:
        break
    idx += 1

for r in rows:
    for el in rol:
        if el >= r[1][0] and el < r[1][1]:
            r[2] += 1
        
Σfi = len(rol)  
Σfri = 0  

for idx, el in enumerate(rows):
    n = 0
    if idx == 0:
        # rows[idx][2] = el[2]
        rows[idx].append(el[2])
        rows[idx].append(round(el[2] / Σfi, 4))
        rows[idx].append(round(el[3] / Σfi, 4))
        Σfri += el[4]
    else:
        rows[idx].append(rows[idx-1][3] + rows[idx][2])
        rows[idx].append(round(el[2] / Σfi, 4))
        rows[idx].append(round(el[3] / Σfi, 4))
        Σfri += el[4]
     
# FORMATING    
for r in rows:
    r[1] = f'{r[1][0]} |-- {r[1][1]}'
        
df = pd.DataFrame(data = rows, columns = ["i", data_type, "fi", "Fi", "fri", "Fri"]) 

print("\n")
print(df.to_string(index=False))
print(f'\nΣfi = {Σfi}')
print('\nΣfri =', round(Σfri, 4), "\n")
print("\nSource:",source)
print("\n")

