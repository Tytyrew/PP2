class dog:
    def __init__(self,type):
        self.type = type
class pet(dog):
    def __init__(self,name):
        self.name = name
        super().__init__("giga")