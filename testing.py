fname=input("enter filename:")
stri=input("enter string")
with open(fname,'r') as f:
    for line in f:
        if stri in line:
            print(line)
