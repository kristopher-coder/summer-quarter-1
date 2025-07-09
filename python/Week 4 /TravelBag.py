bedroom = ["Hat", "Shoes", "Sunscreen", "Socks"] 



travelBag = [] 


print("Pack your bags")
print("Enter the index of an item you'd like to move from your room to a the bag.")
print("Type 100 when you are 'done' packing.\n")
print("Your bedroom items")
for item in bedroom: 
    print(item) 
item =int(input("Item Index: "))


while item != 100:
    travelBag.append(bedroom[item])
    bedroom.remove(bedroom[item])
    print("\nYour Bedroom:") 
    print(bedroom) 
    print("\nYour Travel Bag:")
    print((travelBag))
    item = int(input("Item Index: "))