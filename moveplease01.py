#!/usr/bin/python3

import shutil
import os

#change to starting dir
os.chdir("/home/student/mikerauer")

#moves file to another dir
shutil.move('raynor.obj', 'ceph_storage/')

#ask user to pick a new name
xname = input('What is the new name for kerrigan.obj?')

####no workie
#moves file and renames based on user input
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


