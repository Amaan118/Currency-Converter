def inrToOther():
    try:
        for data in currencyDict.keys():
            print(data)

        currency = input("\nEnter Any Currency from Above : ")
        currency = currency.title()
        amount = int(input(f"Enter Amount in INR to Convert to {currency} : "))
        value = float(currencyDict[currency])
        print(f"{amount} INR is equivalent to {value * amount}")

    except KeyError:
        print("Please Choose a Currency from Above")


def otherToInr():
    try:
        for data in currencyDict.keys():
            print(data)

        currency = input("\nEnter Any Currency from Above : ")
        currency = currency.title()
        amount = int(input(f"Enter Amount in {currency} to Convert to INR : "))
        value = float(currencyDict[currency])
        print(f"{amount} {currency} is equivalent to {amount / value} INR")

    except KeyError:
        print("Please Choose a Currency from Above")


with open("4_Currency_Info.txt", "r") as f:
    data = f.readlines()

currencyDict = {}
for line in data:
    nation = line.split("\t")
    currencyDict[nation[0]] = nation[1]


choice = int(input('''
        ====== MENU =====
        1. INR to Other 
        2. Other to INR
        3. Exit
        
        Enter Choice : '''))

if choice == 1:
    inrToOther()
elif choice == 2:
    otherToInr()
elif choice == 3:
    exit()
else:
    print("\nInvalid Choice ")
