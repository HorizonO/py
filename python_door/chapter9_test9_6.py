#继承9.1
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("\nRestaurant name is " + self.restaurant_name)
        print("Cuisine_type is " + self.cuisine_type)
    def open_restaurant(self):
        print("Restaurant is opening!\n")
new_restaurant = Restaurant('KFC','Fried')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
class IceCreamStand(Restaurant):
    def __init__(self,flavors):  #存储各种口味的冰淇淋
        self.flavors = flavors
    def showIceScream(self):
        print("This IceCream's flavors is:" + self.flavors.title())
new_icecream = IceCreamStand('banana')
new_icecream.showIceScream()