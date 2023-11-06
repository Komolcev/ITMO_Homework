import random


class Teacher:
    def __init__(self, name):
        self.name = name

    def assign_task(self, pupil, task):
        pupil.receive_task(task)

    def check_task(self, pupil, task_description):
        mark = Marks.get_mark()
        pupil.receive_feedback(mark, task_description)


class Pupil:
    def __init__(self, name):
        self.name = name
        self.task = None
        self.mark = None

    def receive_task(self, task):
        self.task = task

    def receive_feedback(self, mark, task_description):
        self.mark = mark
        print(f"{self.name} получил оценку {self.mark} по {task_description}")


class Marks:
    @staticmethod
    def get_mark():
        marks = {2: "плохо", 3: "удовлетворительно", 4: "хорошо", 5: "отлично"}
        return marks[random.choice(range(2, 6))]


class Task:
    def __init__(self, task_description):
        self.task_description = task_description
        self.mark = None


teacher = Teacher("Преподаватель")
pupil1 = Pupil("Ученик 1")
pupil2 = Pupil("Ученик 2")
pupil3 = Pupil("Ученик 3")

task_description1 = "задаче 1"
task1 = Task(task_description1)
task_description2 = "задаче 2"
task2 = Task(task_description2)

teacher.assign_task(pupil1, task1)
teacher.assign_task(pupil1, task2)
teacher.assign_task(pupil2, task1)
teacher.assign_task(pupil2, task2)
teacher.assign_task(pupil3, task1)
teacher.assign_task(pupil3, task2)

pupil1.receive_task(task1)
pupil1.receive_task(task2)
pupil2.receive_task(task1)
pupil2.receive_task(task2)
pupil3.receive_task(task1)
pupil3.receive_task(task2)

teacher.check_task(pupil1, task_description1)
teacher.check_task(pupil1, task_description2)
teacher.check_task(pupil2, task_description1)
teacher.check_task(pupil2, task_description2)
teacher.check_task(pupil3, task_description1)
teacher.check_task(pupil3, task_description2)
