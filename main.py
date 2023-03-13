from item import Item
from phone import Phone

item1 = Item('MyItem', 750)
item1.name = 'OtherItem'
print(item1)

'''
#creating instance of a class
item1 = Item('Phone', 100, 2)
print(item1.calculate_discounted_price())

#calling method
#item1.calculate_total_price()

#print(Item.__dict__) #Prints all attributes of object
#print(item1.__dict__) #Prints all attributes of object

item2 = Item('Laptop', 1000, 3)
item2.pay_rate = 0.7
print(item2.calculate_discounted_price())
'''