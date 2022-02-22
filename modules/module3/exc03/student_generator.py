import csv
from random import random
import course
import data_sheet
import Student
import os


def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as out_file_obj:
        output_writer = csv.writer(out_file_obj, delimiter='\t')
        for elements in lst:
            output_writer.writerow(elements)

if __name__=="__main__":
    path = '/python_4sem/modules/module3/exc03/'
    grades = [-3,2,4,7,10,12]
    availale_courses = ["Python", "Robotter", "Auto kode", "Sys", "Security", "GameDev"]
    gender = ["Male", "Female"]
    male_names = ["Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas"]
    female_names = ["Olivia", "Emma", "Ava", "Charlotte", "Sophia", "Amelia", "Isabella", "Mia"]
    last_names = ["Stevenson", "Donovan", "Cook", "Matthams", "Cherry", "Goldsmith", "Landry", "Mccarthy", "Tillman", "Preece"]

    def student_generator(n):
        stu_list = list([])
        for i in range(n):
            _gender = random.choice(gender)
            if _gender == "male":
                stu_list.append(
                    Student(
                        random.choice(male_names) + random.choice(last_names),
                        _gender,
                        data_sheet(random.sample(availale_courses,3)),
                        random.choice(grades),
                        random.randint(1000,9999)
                    )
                )
        else:
            stu_list.append(
                    Student(
                        random.choice(female_names) + random.choice(last_names),
                        _gender,
                        data_sheet(random.sample(availale_courses,3)),
                        random.choice(grades),
                        random.randint(1000,9999)
                    )
                )
        