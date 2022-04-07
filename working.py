uI = int(input("Enter a Number: "))
x = 1
while x < 10:
    if x < uI:
        print("skipping work {}".format(x))
        x = x + 1
        continue
    print(x)
    if x == 8:
        print("Enough of work")
        break
    x = x + 1
print("Done")
