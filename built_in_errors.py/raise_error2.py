class mobile:
     def __init__(self,name):
        self.name=name
class mobilestore:
    def __init__(self):
        self.mobile=[]
    def add_mobile(self,new_mobile):
        self.mobile.append(new_mobile)

oneplass=mobile("oneplass 7t")
samsung="galexy 2345"
mobostore=mobilestore() 
print(mobostore.add_mobile(samsung))  
