import math;

def isPrime(num):
    if(num==2 or num==3):
        return True;
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            return False;
    return True;

def numToList(num):
    string = str(num);
    listOfDigit = [];
    for digit in string:
        listOfDigit.append(int(digit));
    return listOfDigit;

def listToNum(listOfDigit):
    num = map(str, listOfDigit);
    num = ''.join(num);
    num = int(num);
    return num;

counter = 0;
for i in range(2,1000000):
    if (isPrime(i)):
        isCircularPrime = True;
        listOfDigit = numToList(i);
        for j in range(len(listOfDigit)):
            rotatingList = (listOfDigit[j:] + listOfDigit[:j]);
            if(not isPrime(listToNum(rotatingList))):
                isCircularPrime = False;
        if(isCircularPrime):
            counter+=1;
    else:
        pass;
print counter;
