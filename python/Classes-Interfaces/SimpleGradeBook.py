class SimpleGradeBook:
    def __init__(self):
        self.grades = {}
    
    def add_student(self, student):
        if student not in self.grades:
            self.grades[student]= {}
        else:
            print(f"Student {student} already exists.")
    
    def add_grade(self, student, subject, grade):
        if student not in self.grades:
            print(f"student {student} doesn't exist.")
            return
        if subject not in self.grades[student]:
            self.grades[student][subject] = []
        self.grades[student][subject].append(grade)

    def get_student_grades(self, student):
        return self.grades.get(student, "Student not found")
    
    def average_grade(self, student):
        grade_dict = self.grades.get(student)
        if grade_dict is None:
            return "Student not found"
        total = 0
        count = 0

        for grades in grade_dict.values():
            total += sum(grades)
            count += len(grades)
            
        if count == 0:
            return "No grades available"
        
        return total/count
        
    def print_all(self):
        for student, subjects in self.grades.items():
            print(f"\n {student}")
            for subject, grade_list in subjects.items():
                print(f" - {subject}: {grade_list}")



grade_book = SimpleGradeBook()
grade_book.add_student("Aruna")
grade_book.add_grade("Aruna", "Maths", 90)
print(grade_book.get_student_grades("Aruna"))
grade_book.average_grade("Aruna")
grade_book.print_all()

grade_book.add_student("shresta")
grade_book.add_grade("shresta", "Maths", 90)
grade_book.add_grade("shresta", "Maths", 93)
print(grade_book.get_student_grades("shresta"))
grade_book.average_grade("shresta")
grade_book.print_all()


# implement weighted scores with multiple classes for 
# Subject, Student, and Grade Book