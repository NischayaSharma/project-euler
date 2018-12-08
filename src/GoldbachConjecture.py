import math;

def isPrime(num):
    if(num==2 or num==3):
        return True;
    if(num==1):
        return False;
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            return False;
    return True;

def isPerfSq(num):
    return int(math.sqrt(num))**2 == num;

def goldRight(num):
    goldbachRight = False;
    for j in range(num,0,-1):
        if(isPrime(j)):
            left = num-j;
            n = left/2;
            if(left%2==0):
                if(isPerfSq(n)):
                    print num,j,n;
                    goldbachRight = True;
    return goldbachRight;

try:
    i=1;
    while True:
        if(not isPrime(i)):
            if(not goldRight(i)):
                print i;
                break;
        i+=2;
except Exception as e:
    print goldbachRight;
    print e;
