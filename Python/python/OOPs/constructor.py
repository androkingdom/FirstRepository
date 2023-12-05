class emp:
    def __init__(self , name):
        self.name = name
    def call_emp(self):
        print(f"Employee Name : {self.name}")

rohanEMP = emp("Rohan")
rohanEMP.call_emp()
