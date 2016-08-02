class student():
    def __init__ (self,name,gender,age,grade,languages_known,classes): #constructor - Special function called when object is created
        self.name = name #Stores name in object
        self.gender = gender #Stores gender in object
        self.age = age
        self.grade = grade # Stores grade in function
        self.friends= []
        self.special_friend = []
        self.languages_known = languages_known
        self.family = []
    
    def promote(self):
        self.grade += 1
   
    def add_friend(self, newfriend):
        self.friends.append(newfriend)

    def add_specialfriend(self):
        self.special_friends.append(newfriend)