#!/usr/bin/env python3
""" list methods!! """
def main():

   # proto = ["ssh", "http", "https"]
   # print(proto)
   # print(proto[1])
   # proto.extend("dns")
   # print(proto)
    #!/usr/bin/env python3
    proto = ["ssh", "http", "https"]
    protoa = ["ssh", "http", "https"]
    print(proto)
    proto.append("dns") # this line will add
   # "dns" to the end of our list
    protoa.append("dns") # this line will add
   # "dns" to the end of our list
    print(proto)
    proto2 = [ 22, 80, 443, 53 ] # a list of
   # common ports
    proto.extend(proto2) # pass proto2 as an
   # argument to the extend method
    print(proto)
    protoa.append(proto2) # pass proto2 as an
   # argument to the append method
    print(protoa)
    #NEED TO FIGURE OUT HOW TO MAKE PROTOA A STR
    str(protoa.pop([3]))
    print(f"this is the 4th item poped out of the protoa list: {protoa}")

main()
