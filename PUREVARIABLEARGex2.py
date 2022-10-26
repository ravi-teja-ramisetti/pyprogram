#PureVarArgsEx2
def disp(*a):
    print("-"*50)
    print("NUMBER OF VALUES IN a=",len(a))
    print("-"*50)
    for val in a:
        print("{}".format(val))
disp(10,20,30)
disp(22,33,44,55)
disp(12,13,14,15,16)
disp("teja","lucky","akarsh")