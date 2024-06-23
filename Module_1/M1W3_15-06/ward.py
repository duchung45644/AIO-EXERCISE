class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name, citizen=None):
        if citizen is None:
            citizen = []
        self.name = name
        self.citizen = citizen

    def add_person(self, person):
        self.citizen.append(person)

    def describe(self):
        print(f"Ward name: {self.name}")
        print("Ward citizen:")
        for person in self.citizen:
            print("\t", end="")
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.citizen:
            if person.__class__.__name__ == "Doctor":
                count += 1

        return count

    def sort_age(self):
        for i in range(len(self.citizen)):
            for j in range(len(self.citizen) - i - 1):
                if self.citizen[j].yob < self.citizen[j + 1].yob:
                    self.citizen[j], self.citizen[j + 1] = (
                        self.citizen[j + 1],
                        self.citizen[j],
                    )

    def compute_average(self):
        _sum = 0
        count = 0
        for person in self.citizen:
            if person.__class__.__name__ == "Teacher":
                _sum += 2024 - person.yob
                count += 1
        return _sum / count


if __name__ == '__main__':
    # Example
    # 2(a)
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()

    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()

    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()

    # 2(b)
    print()
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    # 2(c)
    print(f"\nNumber of doctors : { ward1.count_doctor ()}")

    # 2(d)
    print("\nAfter sorting Age of Ward1 people ")
    ward1.sort_age()
    ward1.describe()

    # 2(e)
    print(f"\nAverage year of birth ( teachers ): { ward1.compute_average ()}")
