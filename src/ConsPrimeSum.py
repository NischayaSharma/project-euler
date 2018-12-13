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
for i in range(1,101):
    sum = 0;
    if(isPrime(i)):
        for j in range(1,i):
            if(isPrime(j)):
                sum+=j;
                if(sum==i):
                    maxI = sum;
                    break;
print maxI;
