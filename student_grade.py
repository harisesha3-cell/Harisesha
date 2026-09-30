class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # List of 3 subject marks
        
    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def display_grade(self):
        avg = self.calculate_average()
        
        # Determine grade based on average
        if avg >= 90:
            grade = "A+"
        elif avg >= 80:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "F"
            
        print(f"\nStudent Name: {self.name}")
        print(f"Total Marks: {self.calculate_total()}")
        print(f"Average: {avg:.2f}")
        print(f"Grade: {grade}")

student = Student("Hari", [85, 92, 78])
student.display_grade()
