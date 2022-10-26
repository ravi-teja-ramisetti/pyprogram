#program for generating the inner for loop in while loop statement
#FORINWHILELOOP
i=1
while(i<6):
    print("-"*50)
    print("value of i----outer loop: {}".format(i))
    print("-"*50)
    for j in range(1,5):
        print("value of j----inner loop: {}".format(j))

    else:
        print("out of loop")
        i=i+1
else:
    print("program executed!!!")