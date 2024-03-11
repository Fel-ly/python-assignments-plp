colors = ["blue","green","white","Yellow","brown", "cream"]
color_I_want = "white"

length = len(colors)
count = 0

while count < length:
    print(colors[count])

    if colors[count] == color_I_want:
        print("They have the color I want!")
        break
    count +=1