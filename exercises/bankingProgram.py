import time
account = {
    "name":"",
    "money":0,
    "age":""
}

def open_account():
    account["name"] = input("What's your name? ")
    account["age"] = input("What's your age? ")

def show_balance():
    return account["money"] if not account["money"] == "" else "You have no money"

def deposit():

    money = float(input("Enter an amount to be deposited: "))
    if(money <= 0):
        print("\nPlease, deposit a valid amount.")
        return 0
    else:
        account["money"] = float(account["money"] + money)
        print(f"Value deposited: {money}")

def with_draw():

    money = float(input("Enter an amount to be with drew: "))
    if money > float(account["money"]):
        print("You don't have enough money")
        return 0
    else:
        account["money"] -= money
        print(f"Money with drew: {money}")

def main():
    is_running = True
    while is_running:

        if account["name"] == "":
            open_account()
        else:
            print("*******************")
            print("  BANKING PROGRAM")
            print("*******************")
            choise = int(input("1.SHOW BALANCE\n2.DEPOSIT\n3.WITHDRAW\n4.EXIT\n"))
            match choise:
                case 1:
                    print(show_balance())
                case 2:
                    deposit()
                case 3:
                    with_draw()
                case 4: 
                    is_running = False
                case _:
                    print("Not a valid option")
        time.sleep(2)        

if __name__ == "__main__":
    main()