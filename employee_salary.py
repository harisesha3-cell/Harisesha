class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = 0.20 * self.basic_salary
        da = 0.10 * self.basic_salary
        total_salary = self.basic_salary + hra + da
        return hra, da, total_salary

    def display(self):
        hra, da, total_salary = self.calculate_salary()
        print(f"Employee name: {self.name}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"HRA 20%: {hra}")
        print(f"DA 10%: {da}")
        print(f"Total Salary: {total_salary}")


emp = Employee("Hari", 40000)
emp.display()
