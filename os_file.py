"""
this python code for take source file and
merge into list for further operation

"""

import os
import csv
import logging

logging.basicConfig(filename='Server.log',level=10,filemode='w',
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')
log =  logging.getLogger(str(__file__).split('/')[-1])

try:
    log.info("finding file on source location")
    os.chdir(r'C:\Users\AHMADKHAN\Desktop\Escodeen\Database\Source_file')
    log.info(f"took source file from {os.getcwd()}")
    list_of_file = os.listdir('.')
    list_count = [lst for lst in list_of_file if lst.endswith('.csv')]
    if len(list_count)<=0:
        raise Exception("FileNotAvailableException")

except Exception:
    log.warning(f"There is no filr available on {os.getcwd()}")
    os.chdir(r'C:\Users\AHMADKHAN\Desktop\Escodeen\Database\Source')
    log.info(f"took source file from {os.getcwd()}")
    list_of_file = os.listdir('.')
    list_count = [lst for lst in list_of_file if lst.endswith('.csv')]


add_list = []
for i in list_count:
    with open(i) as fp:
        read = csv.reader(fp)
        for i in read:
            if i in add_list:
                continue
            else:
                add_list.append(i)


print(add_list)