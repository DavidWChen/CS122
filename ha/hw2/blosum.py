

import sys

def populate_matrix(matrixFile):
    lines = matrixFile.readlines()
    matrixFile.close()
    dictaa = {}
    aminoacidstring = lines[0]
    aminoacidstring = aminoacidstring.split()

    i = 1
    while i <= (len(lines)-1):
        row = lines[i]
        row = row.split()

        j = 1
        for character in row[1:25]:
            dictaa[aminoacidstring[i-1],aminoacidstring[j-1]] = character
            j+=1
        i+=1

    print(dictaa)

if __name__ == "__main__":
  filename = sys.argv[1]
  f=open(filename, "r")
  populate_matrix(f)