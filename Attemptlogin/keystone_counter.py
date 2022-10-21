#!/usr/bin/env python3

"""parse through wsgi file and count the amout of login fails"""

login_fails = 0

with open("/home/student/mycode/Attemptlogin/keystone.common.wsgi", "r") as keystone_file:
    for line in keystone_file:
        if "- - - - -] Authorization failed" in line:
            login_fails += 1
            print(f"you have {login_fails} login fails")

