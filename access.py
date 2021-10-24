def access(i):
    sel = None
    while sel != '9':
        sel = input("Enter 0 to do a money transfer, enter 1 to check your balance or enter 9 to quit: ")

        if sel == '1':
            print()
            print("The money in your account is: " + i['Money'] + "€")
        if sel=='0':
            send_money(i)


    return

