def isAmicable(num):
    sumOfDivisor = 0;
    sumOfSumOfDivisor = 0;
    for i in range(1,num):
        if num%i==0:
            sumOfDivisor+=i;
    for j in range(1,sumOfDivisor):
        if sumOfDivisor%j==0:
            sumOfSumOfDivisor+=j;
    return sumOfSumOfDivisor==num;

def main():
    sum = 0;
    for i in range (1,10001):
        if isAmicable(i):
            sum+=i;
            print sum,"\t",i;

main();
