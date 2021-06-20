MenuList = []

def ShowBill():
    SumPriceFood = 0
    print("---- My Food----")
    for number in range(len(MenuList)) :
        print(MenuList[number][0],MenuList[number][1])
        SumPriceFood += int(MenuList[number][1])
    
    print("Total :",SumPriceFood)

       

while True :
    MenuName = input("Plase Enter Menu :")
    if MenuName.capitalize() == "Exit" :
        break
    else :
        MenuPrice = input("Price :")
        MenuList.append([MenuName,MenuPrice])
        
ShowBill()    

