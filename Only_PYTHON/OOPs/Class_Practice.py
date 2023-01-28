# Question from :

# https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-1-create-a-class-with-instance-attributes

# Question - 1 
#not done

# Question - 2 
# class Vechile:
#     pass

# Question - 3 
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
    
# class bus(Vehicle):
#     def info(self):
#         print(f"Vechile name : {self.name} Speed : {self.max_speed} Mileage : {self.mileage}")
# School = bus("School Volvo",180,12)
# School.info()

# Question - 4
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class bus(Vehicle):
    pass
obj = Vehicle("School Volvo",180,12)
obj.seating_capacity(50)
# -------- not completed -------- 