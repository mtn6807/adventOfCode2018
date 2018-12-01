total = 0
x = set({})
run = True
while(run == True):
    file = open("input.txt")
    for line in file:
        newtotal = total + int(line)
        #print("current frequency ",total , ", change of " , line,"; resulting frequency ",newtotal,"\n")
        total = newtotal
        if(total in x):
            print("the total is",total)
            run = False
            break
        else:
            x.add(newtotal)
    file.close()
