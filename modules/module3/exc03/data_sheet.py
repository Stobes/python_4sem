import course

class data_sheet():
    def __init__(self, courses=[]):
        self.courses = courses

    def get_grade_as_list(self):
        return list([course.grade for course in self.courses if course.grade != "blank_if_not_chosen"])
