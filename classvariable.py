class Employee:
    # --- Class Variables ---
    company_name = "Google"  
    total_employees = 0        

    def __init__(self, name, role):
        # --- Instance Variables ---
        self.name = name       
        self.role = role       
        
        Employee.total_employees += 1

print(f"Initial Employee Count: {Employee.total_employees}")  

#  Creating  object instances
emp1 = Employee("Greesha", "AI/ML Engineer")
emp2 = Employee("Tejaswi", "Account Manager")

#  Instance Variables 
print(f"{emp1.name} works as a {emp1.role}")  
print(f"{emp2.name} works as a {emp2.role}")  

#  Class Variables 
print(emp1.company_name)  
print(emp2.company_name)  
print(f"Total Employees: {Employee.total_employees}") 

# 5. Changing the class variable affects all instances
Employee.company_name = "IBM"
print(emp1.company_name)  
print(emp2.company_name) 
