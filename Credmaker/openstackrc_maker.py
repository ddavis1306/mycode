#!/usr/bin/env python3
"""prompt the user for the values surrounded by angle brackets.
 Then we'll write out the file."""

 #define output file:
outFile = open("admin.rc", "a")#a = append
# export OS_AUTH_URL=<url-to-openstack-identity>
osAUTH = input("whats your os auth url? ")
print("export OS_AUTH_URL=" + osAUTH, file=outFile)
# export OS_IDENTITY_API_VERSION=3
print("OS_IDENTITY_API_VERSION=3", file=outFile)
# export OS_PROJECT_NAME=<project-name>
osPROJ = input("whats your OS project name? ")
print("export OS_PROJECT_NAME="+ osPROJ,file=outFile)
# export OS_PROJECT_DOMAIN_NAME=<project-domain-name>
osProDom = input("whats your OS Domain? ")
print("export OS_PROJECT_DOMAIN_NAME="+ osProDom,file=outFile)
# export OS_USERNAME=<username>
osUSER = input("enter your username: ")
print("export OS_USERNAME="+ osUSER,file=outFile)
# export OS_USER_DOMAIN_NAME=<user-domain-name>
osUSERDOM = input("enter user domain name: ")
print("export OS_USER_DOMAIN_NAME="+ osUSERDOM,file=outFile)
# export OS_PASSWORD=<password>  # (optional-- but we'll set it in ours)
osPASS = input("What is the OS_PASSWORD? ")
print("export OS_PASSWORD=" + osPASS, file=outFile)
outFile.close()
