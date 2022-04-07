def countdown(n=20):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)
