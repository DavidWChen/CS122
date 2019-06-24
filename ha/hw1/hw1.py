import sys

def one(data):
    a,b=data.split(' ')
    print (int(a)**2+int(b)**2)

def two(data):
    string=data.split('\n')[0]
    w,x,y,z=map(int,data.split('\n')[1].split(' '))
    print (string[w:x+1]+' '+string[y:z+1])

def three(data):
    a,b=map(int,data.split(' '))
    sum=0
    for x in range (a,b):
        if x%2 == 1:
            sum=sum+x
    print(sum)

def four(data):
    lines = data.split('\n')
    file = open('ans.txt','w') 
    #line 1 is index 0
    for x in range(1,len(lines),2):
        file.write(lines[x]+'\n')

def five(data):
    words = data.split()
    word_dict = {}
    for word in words:
        #for x in range(0, len(words)):
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    file = open('ans.txt','w') 
    for key, value in word_dict.items():
        file.write(str(key) + ' ' + str(value) + '\n')

def six(data):
    numA,numC,numG,numT=0,0,0,0
    for char in data:
        if char=='A':
            numA=numA+1
        elif char=='C':
            numC=numC+1
        elif char=='G':
            numG=numG+1
        elif char=='T':
            numT=numT+1
        else:
            pass
    print('{} {} {} {}'.format(numA,numC,numG,numT))

def seven(data): 
    letters = data.split('\n')[0].split()
    length = int(data.split('\n')[1][0])
    permutations = []
    for x in range(len(letters)):
        for y in range(x+1, len(letters)): 
            permutations.append(letters[x]+letters[y])
    print(permutations)

def seven(data): 
    letters = sorted(data.split('\n')[0].split())
    length = int(data.split('\n')[1][0]) 
    seven_rec(letters, '', length) 
  
def seven_rec(letters, nub, length): 
    if (length == 0): 
        print(nub) 
        return
    for x in range(len(letters)): 
        nubbin = nub + letters[x] 
        seven_rec(letters, nubbin, length - 1)
        

if __name__ == "__main__":
    filename = sys.argv[1]
    f=open(filename, "r")
    data = f.read()
    seven(data)
