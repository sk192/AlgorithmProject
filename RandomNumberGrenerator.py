import  os, sys, random


afile = open("Input.txt", "w")

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(-20, 100000))
    afile.write(line+str("\n"))
    print(line)

afile.close()

