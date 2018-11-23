 Develop a python script that will prompt the user for a string and a file name, and then
print all lines in the file that contains the string entered by the user.
fname=input("enter filename:")
stri=input("enter string")
with open(fname,'r') as f:
    for line in f:
        if stri in line:
            print(line)
