if __name__ == '__main__':
    # oop
    """une classe
    commence tjrs par une lettre majuscule et doit etre au sigulier
    """

    class Student:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

    s = Student("Jean", "Paul")
    print(s.first_name, s.last_name)
