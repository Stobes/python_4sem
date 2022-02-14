import os

if __name__=="__main__":

    def get_file_names(folderpath,out='output.txt'):
        with open(out, 'w') as file_obj:
            for f in os.listdir(folderpath):
               file_obj.write(f+'\n')

    #get_file_names('4sem_python/modules/module2/', '4sem_python/modules/module2/foldertest.txt')

    def get_all_file_names(folderpath, out='output.txt'):
        with open(out, 'a') as file_obj:
            for f in os.listdir(folderpath):
                if not os.path.isdir(folderpath + f):
                    file_obj.write('\t'+f+'\n')
                else:
                    file_obj.write(f+'\n')
                    get_all_file_names(os.path.join(folderpath,f), out)

    #get_all_file_names('4sem_python/modules/module2/', '4sem_python/modules/module2/folder_test2.txt')

