class Grade():
    def __init__(self,school,banji):
        self.school = school
        self.banji = banji
    def stulist(self):
        return "学生名单：张力，李晶晶，高星等15位同学。"

    def tealist(self):
        return "老师名单：高老师，丁老师，刘老师。"
g1 = Grade("天河学院","计科2班")

print(g1.school+"的"+g1.banji+"的"+str(g1.stulist())+"和"+str(g1.tealist()))