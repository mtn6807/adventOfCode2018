file = open("input.txt")

array1 = []
array2 = []

for line in file:
    #print(line)
    array1.append(line)
    array2.append(line)
gotOne = False
for word in array1:
    #print(word,"\n")
    for otherword in array2:
        #print(otherword,"\n")
        anser =""
        counter = 0
        diff=0
        for i in range(0,len(word)):
            if word[i]!=otherword[i]:
                diff+=1
            else:
                anser+=word[i]
            counter+=1
            
        if diff == 1:
            print(anser)
            gotOne = True
            break
    if gotOne:
        break
