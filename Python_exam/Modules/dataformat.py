from tokenize import String


def clean_data(scraping_list):

    new_list = []

    for sub_category in scraping_list[0]:

        prod_update = []

        for j in range(len(sub_category)):

            if '/Stk' in sub_category[j][2]:
                sub_category[j][2] = sub_category[j][2][:-5]

            if '/Kg' in sub_category[j][2]:
                sub_category[j][2] = sub_category[j][2][:-4]

            if '/L' in sub_category[j][2]:
                sub_category[j][2] = sub_category[j][2][:-3]

            if '.-' in sub_category[j][1]:
                sub_category[j][1] = sub_category[j][1][:-3]

            if type(sub_category[j][1]) == str:
                sub_category[j][1] = float(sub_category[j][1])

            if type(sub_category[j][2]) == str:
                sub_category[j][2] = float(sub_category[j][2])

            if scraping_list[1][scraping_list[0].index(sub_category)].lower() in sub_category[j][0].lower() and 'm.' not in sub_category[j][0]:
                prod_update.append(sub_category[j])

        new_list.append(prod_update)

    return new_list