print("Welcome to Dominas Pizza Deliveries.!")
bill = 0
statement = True
while statement:
    size_of_pizza =input("What size Pizza do you really want ? S, L or M: ").upper()
    if size_of_pizza == "S":
        bill = 15
        statement = False
    elif size_of_pizza == "L":
        bill = 20
        statement = False
    elif size_of_pizza == "M":
        bill = 25   
        statement = False
    else:
        print(f"Seems like you entered wrong input \'try with S or L or M \n")
        statement = True
peporonie =input("Do you want Peporonie in your Pizza ? Y or N: ").upper()
if peporonie == "Y":
    if size_of_pizza == "S":
        bill+=2
        print("additional '$ 2'")
    else:
        bill+=3
        print("additional '$ 3'")                         
         
cheese = input("Do you want extra Cheese? Y or N: ").upper()

if cheese =="Y":
    bill+=1 
    print("additional '$ 1' for cheese")
print(f"Your finall Bill is '${bill} ")
print ("Thanks for visiting Python Pizza Deliveries.")
