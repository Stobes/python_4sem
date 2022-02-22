import data_sheet
import course


class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url


    def get_avg_grade(self):
        return sum(data_sheet.get_grade_as_list())/len(data_sheet.get_grade_as_list)

    