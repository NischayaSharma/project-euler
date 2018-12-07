def decToBin(num,binNum):
    if num > 1:
        decToBin(num // 2,binNum);
    binNum.append(num%2);
    return listToNum(binNum);

def listToNum(listOfDigit):
    num = map(str, listOfDigit);
    num = ''.join(num);
    num = int(num);
    return num;

def isPalindrome(num):
    paliNum=0;
    n=num;
    while (n):
        paliNum = (10*paliNum) + (n%10);
        n/=10;
    return paliNum==num;

sum = 0;
for i in range(1000000):
    if(isPalindrome(i) and isPalindrome(decToBin(i,[]))):
        sum+=i;
print sum;
