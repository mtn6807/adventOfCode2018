file = open("input.txt")

twos = 0
threes = 0

for line in file:
    for otherline in file:
        if line != otherline:
            diff = 0
            letter = 'a'
            for x in line:
                for y in otherline:
                    if(x!=y):
                        letter = x
                        diff += 1
            if diff == 1:
                word = ""
                for i in line:
                    if i != letter:
                        word+=i
                print("the word ",word)
                break
