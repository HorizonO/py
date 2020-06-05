#9-1
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

#9-2
second_restaurant = Restaurant("Macdoload","Chicken")
second_restaurant.describe_restaurant()
second_restaurant.open_restaurant()


#9-3
class User():
    def __init__(self,first_name,last_name,sex,email):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.email = email
    def describe_user(self):
        print("This people name is "+self.first_name
              +self.last_name+".\nSex is "+self.sex+
              ".\nEmail is "+self.email)
    def greet_user(self):
        print("Are you OK?")
new_user = User('LI','YOU','MAN','1531532@163.com')
new_user.describe_user()
new_user.greet_user()