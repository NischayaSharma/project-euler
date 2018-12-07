import numpy as np;

def listToNum(listOfDigit):
    num = map(str, listOfDigit);
    num = ''.join(num);
    num = int(num);
    return num;

def numToList(num):
    string = str(num);
    listOfDigit = [];
    for digit in string:
        listOfDigit.append(int(digit));
    return listOfDigit;

arrOfNum = np.arange(1000001);
listOfNum = list(arrOfNum);
listOfDigit = numToList(listToNum(listOfNum));
solution = listOfDigit[0]*listOfDigit[9]*listOfDigit[99]*listOfDigit[999]*listOfDigit[9999]*listOfDigit[99999]*listOfDigit[999999];
print solution;
