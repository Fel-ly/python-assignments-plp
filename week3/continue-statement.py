# this code demonstrates the use of a contnue statement where ages less than 21 are skipped
# and those above 21 are printed out

ages  =  [13, 14, 29, 38, 12, 40, 26, 27, 27]

for age in ages:
    if age < 21:
        continue
    print(age)