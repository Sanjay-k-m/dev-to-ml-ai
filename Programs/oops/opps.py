class employee:
    val = "HDFC"
    def __init__(self,first:str,last:str,email:str) -> None:
        self.first = first
        self.last = last
        self.email = email
        
emp1 = employee("sanjay","Km","sanjaykm@gmail.com")


print(emp1.first)