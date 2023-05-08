from classes.student import showstudent, printing

import platform
if __name__ == '__main__':
    # oop
    """une classe
    commence tjrs par une lettre majuscule et doit etre au singulier
    """

    # class Student:
    #     def __init__(self, first_name, last_name, age):
    #         self.first_name = first_name
    #         self.last_name = last_name
    #         self.age = age

    #     def __str__(self) -> str:
    #         return f"{self.first_name}({self.age})"

    # s = Student("Jean", "Paul", 24)
    # print(s.first_name, s.last_name, s.age)
    # print(s)

    showstudent()

    printing()

    x = platform.system()

    print(x)

# pip freeze > requirements.txt

# pip install -r requirements.txt
