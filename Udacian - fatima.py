class enrollment:
    def __init__(self,enrollment):
        self.enrollment = enrollment
    
    
    
class Udacian:
    def __init__(self, name,city ,enrollment , nanodgree,status,count):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodgree = nanodgree
        self.status = status
        self.count = count
         
    def print_udacian(self):
        print(self.name+' '+self.city+' '+self.enrollment+' '+self.status+' '+self.nanodgree+' '+self.count)
     
        
        
             
p = Udacian('fatima','jeddah','enrolment','full stack ','single ','First time')

p.print_udacian()
