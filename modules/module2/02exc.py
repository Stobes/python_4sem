import csv
import platform
import argparse

def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.read()
    print(content)

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as out_file_obj:
        output_writer = csv.writer(out_file_obj, delimiter='\t')
        for elements in lst:
            output_writer.writerow(elements)

def read_csv(input_file):
    with open(input_file) as i_f:
        reader = csv.reader(i_f)
        #header_row = next(reader)

        lst = [row for row in reader]
    return lst

filename = 'data/country_codes.csv'
out_file = 'data/babies.csv'
baby_lst = ['male', 'white', 'blue']
test_file = '4sem_python/modules/module2/test.csv'
lst = list([])

if platform.system() == 'Windows':
    newline=''
else:
    newline=None

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='A program that bla bla bla..')

    parser.add_argument('csv_path', help='path to csv file')
    parser.add_argument('--file', help='path to the file you want to write csv content to')

    args = parser.parse_args()
    print('file_path:', args.csv_path)
    print('file_dest:', args.file)

    if args.file == None:
       print_file_content(args.csv_path)
    else:
        write_list_to_file(args.file, read_csv(args.csv_path))
    
   
