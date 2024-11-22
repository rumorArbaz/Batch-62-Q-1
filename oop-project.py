class Student:
    def __init__(self, name, grade):
        self.name = name
        self.scores = {}

    def add_score(self, subject, score):
        self.scores[subject] = score 

    def average(self):
        return sum(self.scores.values()) / len(self.scores)

    def is_pass(self):
        for subject, score in self.scores.items():
            if score < 40:
                return f"Fail (failed in {subject})"
        return "Pass"

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if not name.isalpha():
            print("Invalid name. Name should only contain alphabetical characters.")
            return
        self.students[name] = Student(name, None)

    def display_student_performance(self):
        for name, student in self.students.items():
            avg_score = student.average()
            pass_status = student.is_pass()
            print(f"Student: {name}, Average Score: {avg_score:.2f}, Pass Status: {pass_status}")

tracker = PerformanceTracker()

while True:
    student_name = input("Enter student name (or type 'exit' to finish): ")
    if student_name.lower() == 'exit':
        break
    try:
        tracker.add_student(student_name)

        for subject in ['Eng', 'Math', 'Sci']:
            while True:
                try:
                    score = float(input(f"Enter score for {subject} (0-100): "))
                    if 0 <= score <= 100:
                        tracker.students[student_name].add_score(subject, score)
                        break
                    else:
                        print("Invalid score. Score should be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Score should be a number.")
    except Exception as e:
        print(f"Error: {e}")

tracker.display_student_performance()