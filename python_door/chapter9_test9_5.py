class User():
    def __init__(self,first_name,last_name,sex,email,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.email = email
        self.login_attempts = login_attempts
    def describe_user(self):
        print("\nThis people name is "+self.first_name
              +self.last_name+".\nSex is "+self.sex+
              ".\nEmail is "+self.email +"\n"+ str(self.login_attempts)+"次访问。")
    def greet_user(self):
        print("Are you OK?")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
new_user = User('LI','YOU','MAN','1531532@163.com',2)
new_user.describe_user()
new_user.greet_user()

new_user.reset_login_attempts()
new_user.describe_user()