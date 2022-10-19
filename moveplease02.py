#!/usr/bin/env python3

"""doc string"""
"""lab 29"""
"""NOT FINISHED"""
import shutil
import os

def main()
#establish working dir
os.chdir("/home/student/mycode/")

#call (source, destination) to move file 

shutil.move('raynor.obj' , 'ceph_storage/')

#prompt user for new name w/ kerrigan.obj file
xname = input(f"whats the new name of kerrigan.obj?---->")
#rename kerrigan obj
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)

#shutil.copytree
main()
