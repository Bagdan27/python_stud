import asyncio
import random
from typing import List

class Assignment:
    def __init__(self, title: str, max_score: int):
        self.title = title
        self.max_score = max_score
        self.score = None

    async def submit(self):
        time_to_complete = random.uniform(1, 3)
        print(f"Starting assignment '{self.title}', will take {time_to_complete:.2f} seconds.")
        await asyncio.sleep(time_to_complete)
        self.score = random.randint(0, self.max_score)
        print(f"Submitted assignment '{self.title}' with score {self.score}/{self.max_score}.")

class Course:
    def __init__(self, name: str, assignments: List[Assignment]):
        self.name = name
        self.assignments = assignments

    async def complete_course(self):
        print(f"Starting course: {self.name}")
        for assignment in self.assignments:
            await assignment.submit()
        print(f"Completed course: {self.name}")

    def get_average_score(self):
        total_score = sum(a.score for a in self.assignments if a.score is not None)
        total_max = sum(a.max_score for a in self.assignments)
        if total_max == 0:
            return 0
        return total_score / total_max * 100

class Student:
    def __init__(self, name: str):
        self.name = name
        self.courses: List[Course] = []

    def enroll(self, course: Course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course.name}")

    async def study(self):
        print(f"{self.name} starts studying.")
        # Study all courses in parallel
        await asyncio.gather(*(course.complete_course() for course in self.courses))
        print(f"{self.name} finished all courses.")

    def report(self):
        print(f"--- Report for {self.name} ---")
        for course in self.courses:
            avg = course.get_average_score()
            print(f"Course: {course.name}, Average Score: {avg:.2f}%")


async def main():
    assignments_math = [
        Assignment("Algebra Homework", 100),
        Assignment("Calculus Project", 100),
        Assignment("Statistics Quiz", 50)
    ]

    assignments_cs = [
        Assignment("Python Basics", 100),
        Assignment("Data Structures", 100),
        Assignment("Algorithms", 100)
    ]

    math_course = Course("Mathematics", assignments_math)
    cs_course = Course("Computer Science", assignments_cs)


  
    student = Student("Alice")
    student.enroll(math_course)
    student.enroll(cs_course)

    await student.study()
    student.report()

if __name__ == "__main__":
    asyncio.run(main())
