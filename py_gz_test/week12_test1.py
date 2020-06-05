class Person:
    role = 'people'
    def __init__(self,name,money,aggressivity,life_value):
        self.name = name
        self.money = money
        self.aggressivity = aggressivity
        self.life_value = life_value
    def attach(self,dog):
        #person attach a dog
         dog.life_value -= self.aggressivity
    def showValue(self):
        return self.life_value
class Dog:
    role = 'dog'
    def __init__(self,name,breed,aggressivity,life_value):
        self.name = name
        self.breed = breed
        self.aggressivity = aggressivity
        self.life_value = life_value
    def bite(self,people):
        #dog bite person
        people.life_value -= self.aggressivity
    def showValue(self):
        return self.life_value
class Weapons:
    def __init__(self,name,price,aggrv,life_value):
        self.name = name
        self.price = price
        self.aggrv = aggrv
        self.life_value = life_value
    def update(self,people):
        people.money -= self.price
        people.aggressivity  += self.aggrv
        people.life_value += self.life_value
    def prick(self, obj):  # 这是该装备的主动技能,假设攻击力是200
        obj.life_value -= self.aggrv
egg = Person('张蛋蛋',20000,100,1000)    #昵称，财力，攻击力、生命值
print(egg.name,"最初生命值",egg.showValue())
dog=Dog('马小哈','哈士奇',300,500)
print(dog.name,"最初生命值",dog.showValue())   #昵称，品种，攻击力，生命值
lance = Weapons('长矛',200,100,100)      #名称，价格，攻击力，生命值

if egg.money > lance.price: #如果egg的钱比装备的价格多，可以买一把长矛
    lance.update(egg)
    egg.weapon = lance
print(egg.name,"装上武器后的生命值",egg.showValue())
egg.weapon.prick(dog)
print(dog.name,"被攻击后生命值",dog.showValue())
dog.bite(egg)
print(egg.name,"被攻击后的生命值",egg.showValue())
