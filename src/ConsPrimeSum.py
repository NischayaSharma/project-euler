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

sum = 0;
for i in range(1,1001):
    sum = 0;
    if(isPrime(i)):
        for j in range(i,1,-1):
            if(isPrime(j)):
                sum+=j;
                if(sum==i):
                    maxI = sum;
                    break;
print maxI;
