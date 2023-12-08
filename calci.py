import sys
if len(sys.argv)!=4:
    sys.exit(1)
operation= sys.argv[0]
num1=int(sys.argv[1])
num2=int(sys.argv[2])
if operation=="addition":
    print(num1+num2)
elif operation=="subtraction":
    print(num1-num2)
elif operation=="multiplication":
    print(num1*num2)
elif operation=="division":
    print(num1/num2)
