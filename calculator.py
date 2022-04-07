def tax_calculator():
    user_name = input("Hi, Enter you Name : ")
    revenue = []
    i = 0
    while True:
        if i == 0:
            amount = input("Enter You Income / NA : ")
        else:
            amount = input("Enter You Additional Income / NA : ")
        i += 1
        if amount == "NA":
            break
        else:
            revenue.append(int(amount))
    print("Hi {}, Your Income List Values is {}".format(user_name, revenue))
    print("Your Total Income Value is {}".format(sum(revenue)))
    if sum(revenue) <= 250000:
        print("No Taxation for Income")
    elif 25000 < sum(revenue) < 50000:
        print("You Taxation is 10%")
    elif 50000 < sum(revenue) < 10000:
        print("Your Taxation is 20%")
    else:
        print("You Taxation is 30%")
