class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("\nRestaurant name is " + self.restaurant_name)
        print("Cuisine_type is " + self.cuisine_type)
    def open_restaurant(self):
        print("Restaurant is opening!\n")
    def have_number_served(self):
        print("This restaurant have "+str(self.number_served)+" people.")
    def set_number_served(self,people):
        self.number_served = people
    def increment_number_served(self,peoples):
        self.number_served += peoples
new_restaurant = Restaurant('KFC','Fried')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
new_restaurant.set_number_served(12)
new_restaurant.have_number_served()
new_restaurant.increment_number_served(10)
new_restaurant.have_number_served()