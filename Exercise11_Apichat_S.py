userinput = int(input())

for x in range(userinput):
    print(" "*(userinput - 1),end=" ")
    print("*"*((x*2)+1))

    userinput -= 1
    x += 1
