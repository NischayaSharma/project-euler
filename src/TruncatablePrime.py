import math;

def truncate(rightSide, num):
    listOfTrncNums = [];
    string = str(num);
    for i in range(len(string)+1):
        if(rightSide):
            listOfTrncNums.append(string[i:]);
        if(not rightSide):
            listOfTrncNums.append(string[:i]);
    return listOfTrncNums;

def isPrime(num):
    if(num!=''):
        num = int(num);
    else:
        return False;
    if(num==2 or num==3):
        return True;
    if(num==1):
        return False;
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            return False;
    return True;

sum=0;
counter = 0;
i = 9;
while counter<11:
    i+=1;
    if(isPrime(i)):
        isTruncPrime = True;
        listOfRightTrncNums = truncate(True,i);
        listOfLeftTrncNums = truncate(False,i);
        for num in range(len(listOfLeftTrncNums)):
            if(listOfLeftTrncNums[num]==''):
                listOfLeftTrncNums.pop(num);
                break;
        for num in range(len(listOfRightTrncNums)):
            if(listOfRightTrncNums[num]==''):
                listOfRightTrncNums.pop(num);
                break;
        for j in range(len(listOfRightTrncNums)):
            if(not isPrime(listOfRightTrncNums[j]) or not isPrime(listOfLeftTrncNums[j])):
                isTruncPrime = False;
                break;
        if(isTruncPrime):
            print i;
            counter+=1;
            sum+=i;
    else:
        pass;
print sum;
