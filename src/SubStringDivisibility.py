from itertools import permutations as perm;

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

def permOf0to9():
    listOfDigit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    listOfPerm = list(perm(listOfDigit));
    for i in range(len(listOfPerm)):
        listOfPerm[i] = listToNum(list(listOfPerm[i]));
    return listOfPerm;

listOfPerm = permOf0to9();
sum=0;
for num in listOfPerm:
    string = str(num);
    if(len(string)<=9):
        continue;
    else:
        d2d3d4 = (num%1000000000)/1000000;
        d3d4d5 = (num%100000000)/100000;
        d4d5d6 = (num%10000000)/10000;
        d5d6d7 = (num%1000000)/1000;
        d6d7d8 = (num%100000)/100;
        d7d8d9 = (num%10000)/10;
        d8d9d10 = (num%1000)/1;
        if(d2d3d4%2==0 and d3d4d5%3==0 and d4d5d6%5==0 and d5d6d7%7==0 and d6d7d8%11==0 and d7d8d9%13==0 and d8d9d10%17==0):
            sum += num;
print sum;
