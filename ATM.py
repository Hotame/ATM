import ATMArt
import time

balance = 0
withdraw = 0
deposit = 0

while True:
    try:
        PIN = int(input("\n\nKaede : Enter 4 Digit PIN Number -> "))
        if PIN in range(1000, 10000):
            break
    except:
        pass


while True:
    print("\n\nKaede : Kaede ATM Menu Options.")
    print("\n\nChoose [1] To Withdraw.")
    print("\n\nChoose [2] To Deposit.")
    print("\n\nChoose [3] To Check Balance.")
    print("\n\nChoose [4] To EXIT")

    choice = int(input("\n\nKaede : Select Your Choice -> "))

    if choice == 1:
        withdraw = int(input("\n\nKaede : Enter The Money You'd Like To Withdraw -> "))
        if balance >= withdraw:
            balance -= withdraw
            print("\n\nKaede : You've Sucessfully Withdrew The Money.\n")
            print(f"\n\nKaede : Your Current Balance Is ${balance}\n")

        else:
            print("Insufficent Cash.")

    if choice == 2:
        deposit = int(input("\n\nKaede : Enter The Money You'd Like To Deposit -> "))
        balance += deposit
        print("\n\nKaede : You've Sucessfully Deposited The Money\n")
        print(f"\n\nKaede : Your Current Balance Is ${balance}\n")

    if choice == 3:
        print(f"\n\nKaede : Your Current Balance Is ${balance}\n")

    if choice == 4:
        print("..")
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("....")
        time.sleep(3)

        print("\n\nKaede : GoodBye ~")
        exit()
