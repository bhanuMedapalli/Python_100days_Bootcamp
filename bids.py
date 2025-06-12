
button = True
values ={}
while button :
    name_of_person = input("Please enter participent name\n").lower()
    Bid_count = int(input("Please enter bid values\n"))
    Stop_or_new = input ("Stop or new \n").title()
    values[name_of_person] = Bid_count
    if Stop_or_new == "Stop":
        button = False
x=0        
for bid in values:
    if values[bid] > x:
        x=values[bid]
    
print(x)
