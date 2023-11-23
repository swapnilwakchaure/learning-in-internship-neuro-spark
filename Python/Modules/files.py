# f = open('practise.txt', 'w+')
# f.write('this is a text file')
# f.close()


# import os
# file_path = os.getcwd()
# # we get current working directory
# print(file_path)
# # list of files in directory
# print(os.listdir('D:\\New folder'))


# import shutil
# # it moves one source file to another destination
# shutil.move('practise.txt', 'D:\\New folder\\learning-in-internship-neuro-spark\\Python\\TextFile')

# # pip install send2trash
# import send2trash
# # it deletes or trash the provided file
# print(send2trash.send2trash('practise.txt'))


import os

cur_path = os.getcwd()
# print(cur_path)
# cur_path = 'D:\New folder\learning-in-internship-neuro-spark\Python\Modules'

def get_files():
    for folder, sub_folders, files in os.walk(cur_path):
        print('\n')
        print(f'Currently looking at {folder}')
        print('\n')
        print('The subfolders are: ')
        for sub_fold in sub_folders:
            print(f'\t SubFolder: {sub_fold}')
        print('\n')
        print('The files are: ')
        for f in files:
            print(f'\t File: {f}')
        print('\n')

# get_files()


import datetime

# mytime = datetime.time()
mytime = datetime.time(2,20,15)
# print(mytime)
# print(mytime.hour) # mytime.minute, mytime.second
mytime.microsecond


today = datetime.date.today()
# 2023-11-23

# print(today.ctime())
# Thu Nov 23 00:00:00 2023



from datetime import datetime

# mydatetime = datetime(year, month, day, hour, minute, second, microsecond)
mydatetime = datetime(2023,11,23,16,1,30,25)
# print(mydatetime) # 2023-11-23 16:01:30.000025



from datetime import date

date1 = date(2021,11,3)
date2 = date(2022,11,3)

# print(abs((date1-date2))) # 365 days, 0:00:00

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

print(datetime1 - datetime2) # 365 days, 10:00:00
