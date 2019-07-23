#!/usr/bin/python3

#imports modules shell utility and Operating System
import shutil
import os

#changes starting directory
os.chdir("/home/student/mikerauer/")

#copies file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copies directory
shutil.copytree("5g_research/", "5g_research_backup/")
