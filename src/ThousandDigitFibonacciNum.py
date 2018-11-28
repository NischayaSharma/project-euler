def fibonacci(num):
    if (num==0):
        return 0;
    if(num==1):
        return 1;
    return fibonacci(num-1) + fibonacci(num-2);

def numOfDigits(num):
    numOfDigits = 0;
    while (num>0):
        num = num/10;
        numOfDigits += 1;
    return numOfDigits;

def main():
    n=0;
    while(n>=0):
        print n;
        if(numOfDigits(fibonacci(n))>=1000):
            break;
        n+=1;
    print "answer:",n;
main();
