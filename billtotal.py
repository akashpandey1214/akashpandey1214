sum = 0
i=1
while(True):
    price=input(f"enter the price of item {i} or press q to quit \n")
    i=i+1
    if (price!='q'):
        sum =sum+int(price)
        print(f"price so far is {sum}")

    else:
        print(f"your bill total is {sum}")
        break
    


