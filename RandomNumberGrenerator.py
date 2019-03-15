# Generate random numbers in Input.txt file.


import  os, sys, random

afile = open("Input.txt", "w")

for i in range(int(input('How many random numbers do you want?: '))):
    line = str(random.randint(-20, 100000))
    afile.write(line+str("\n"))                   #  Generate Random integer numbers in file Input.txt

afile.close()

