def Login():
    usernameInput = str(input("UserName :"))
    PasswordInput = input("Password :")
    if usernameInput == "Apichat" and PasswordInput == "0831" :
        return True
    else :
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def MenuSelect():
    userSelected = int(input("-->"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    return totalPrice + (totalPrice * vat / 100)

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)



if Login():
    showMenu()
    
    if MenuSelect() == 1 :
        totalPrice = int(input("price :"))
        print(vatCalculator(totalPrice))
    
    elif MenuSelect() == 2 :
        print(priceCalculator())

    else :
        print("The menu you selected cannot be found.")
else:
    print("Error")



    
    
    
    