import os
import random
import shutil

source = 'C:/Users/hadie/Desktop/testseq/viral'
dest = 'C:/Users/hadie/Desktop/testseq/randomvertvirus'
files = os.listdir(source)
no_of_files = len(files) // 10

for file_name in random.sample(files, no_of_files):
    shutil.move(os.path.join(source, file_name), dest)