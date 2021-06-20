MenuList = []
PriceList = []

SumPriceFood = 0

def ShowBill():
    print("---- My Food ----")
    for number in range(len(MenuList)) :
        print(MenuList[number],PriceList[number])

def SumPrice(SumPriceFood):
    for price in PriceList :
        SumPriceFood += price
    print("Total :",SumPriceFood)

while True :
    MenuName = input("Plase Enter Menu :")
    if MenuName.capitalize() == "Exit" :
        break
    else :
        MenuPrice = int(input("Price :"))
        MenuList.append(MenuName)
        PriceList.append(MenuPrice)
ShowBill()    
SumPrice(SumPriceFood)
