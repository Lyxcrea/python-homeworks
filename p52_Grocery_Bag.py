# Program Name: p52_Grocery_Bag.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 11/16/18 - 11/17/18
# Description: Create a class Item which has
# - instance variables: itemName, itemCost
# - class variable: numberItems (gets increased every time a new Item is
# created)
# - a default constructor that allows the user to set itemName and itemCost
# ( the default constructor sets itemName="apple" itemCost=2.49 if the user
# does not specify them)
# - function to show() the item name and cost
# - function to get() and set() the item name and cost
# Create a list named groceryBag. 
# - Fill the list with several Item's such as eggs, milk, carrots, bread, apples, each with different price.
# - use Item.numberItems to show how many items you have created.
# - use a loop to calculate and show the totalCost for all the items in the bag

class Item:
    numberItems = 0    
    
    def __init__(self, itemName = "apple", itemCost = 2.49):
        self.itemName = itemName
        self.itemCost = itemCost
        Item.numberItems += 1

    def show(self):
        print(itemName, itemCost)

    def getItemName(self):
        return self.itemName

    def setItemName(self, newItemName):
        self.itemName = newItemName

    def getItemCost(self):
        return self.itemCost

    def setItemCost(self, newItemCost):
        self.itemCost = newItemCost
    

groceryBag = []
totalCost = 0

eggs = Item("eggs", 2.00)
groceryBag.append(eggs)

milk = Item("milk", 3.50)
groceryBag.append(milk)

carrots = Item("carrots", 0.69)
groceryBag.append(carrots)

bread = Item("bread", 2.50)
groceryBag.append(bread)

apples = Item()
groceryBag.append(apples)

print("Number Of Items: %i" %Item.numberItems)

for i in range(0, len(groceryBag), 1):
    totalCost += groceryBag[i].getItemCost()
    
print("Total Cost: %.2f" %totalCost)
    

'''
>>> 
======= RESTART: C:\Users\Charlize\Documents\Python\p52_Grocery_Bag.py =======
Number Of Items: 5
Total Cost: 11.18
>>>
'''
