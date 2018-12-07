
def sumOfPowerDigits(num,power):
    sum = 0;
    while num:
        sum += (num%10)**power;
        num = num/10;
    return sum;

greatSum = 0;
for i in range(1000000):
    sum = sumOfPowerDigits(i,5);
    if(sum==i):
        greatSum +=sum;
        print i;
print i+1,greatSum;
