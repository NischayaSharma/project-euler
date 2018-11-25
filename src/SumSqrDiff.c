#include "stdio.h"

int main(){
  long int sumOfSqr=0, sqOfSum=0, sum=0, diff=0;
  for(int i=1 ; i<=100 ; i++)
    sumOfSqr+=i*i;
  for(int i=1 ; i<=100 ; i++)
    sum+=i;
  sqOfSum=sum*sum;
  diff=sqOfSum-sumOfSqr;
  printf("%ld",diff);
}
