class enrollment:
    def __init__(self,enrollment):
        self.enrollment = enrollment
    
    
    
class Udacian:
    def __init__(self, name,city ,enrollment , nanodgree,status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodgree = nanodgree
        self.status = status
         
    def print_udacian(self):
        print(self.name+' '+self.city+' '+self.enrollment+' '+self.status+' '+self.nanodgree)
     
        
        
             
p = Udacian('fatima','jeddah','enrolment','full stack ','single')
p2 = Udacian('Doaa','Riyadh','graduate','programming','married')

p.print_udacian()
