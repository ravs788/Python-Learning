class Class1: 
    def m(self): 
        print("In Class1") 
  
class Class2(Class1): 
    def m(self): 
        print("In Class2") 
        super().m() 
  
class Class3(Class1): 
    def m(self): 
        print("In Class3") 
        super().m() 
  
class Class4(Class2, Class3): 
    def m(self): 
        print("In Class4")    
        super().m() 
       
obj = Class4() 
obj.m() 

print(Class4.mro())
print(Class3.mro())
print(Class2.mro())
print(Class1.mro())
