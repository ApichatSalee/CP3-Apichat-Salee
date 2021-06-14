usernameInput = str(input("UserName :"))
PasswordInput = input("Password :")

vat = 7

Apple_price = 30
Mango_price = 20
Pineapple_price = 55
Coconut_price = 150 
Grape_price = 300

if usernameInput == "Apichat" and PasswordInput == "0831" :
    
    print("--------------Welcome Apichat Shop--------------")
    print("1.Apple 30 THB")
    print("2.Mango 20 THB")
    print("3.Pineapple 55 THB")
    print("4.Coconut 150 THB")
    print("5.Grape 300 THB")
    
    userSelected0 = int(input("-->"))
    
    if userSelected0 >= 1 and userSelected0 <= 5  : 
       
        if userSelected0 == 1 :
            userSelected1 = int(input("how many 1 / "+ str(Apple_price) + "THB :"))
            if userSelected1 >= 1 and userSelected1 <= 10000 :

                price = userSelected1 * Apple_price
                
                result = price + (price * vat / 100)
                print("price including tax",result,"THB")   
            
        
        
        elif userSelected0 == 2 :
            userSelected1 = int(input("how many 1 / "+ str(Mango_price) + "THB :"))
            if userSelected1 >= 1 and userSelected1 <= 10000 :

                price = userSelected1 * Mango_price
                
                result = price + (price * vat / 100)
                print("price including tax",result,"THB")   
            
        
        elif userSelected0 == 3 :
            userSelected1 = int(input("how many 1 / "+ str(Pineapple_price) + "THB :"))
            if userSelected1 >= 1 and userSelected1 <= 10000 :

                price = userSelected1 * Pineapple_price
                
                result = price + (price * vat / 100)
                print("price including tax",result,"THB")   
            
        
        elif userSelected0 == 4 :
            userSelected1 = int(input("how many 1 / "+ str(Coconut_price) + "THB :"))
            if userSelected1 >= 1 and userSelected1 <= 10000 :

                price = userSelected1 * Coconut_price
                
                result = price + (price * vat / 100)
                print("price including tax",result,"THB")   
            
        
        elif userSelected0 == 5 :
            userSelected1 = int(input("how many 1 / "+ str(Grape_price) + "THB :"))
            if userSelected1 >= 1 and userSelected1 <= 10000 :

                price = userSelected1 * Grape_price
                
                result = price + (price * vat / 100)
                print("price including tax",result,"THB")  
    
        if userSelected1 < 1 :
            print("too little product")
        elif userSelected1 >= 10000 :
            print("too much product")    


if userSelected0 < 1 or userSelected0 > 5  : 
    print("The product you want is not available.")     



    