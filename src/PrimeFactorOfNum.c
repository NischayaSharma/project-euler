#include "stdio.h"
#include "math.h"
#include "stdbool.h"

bool isPrime(long int num){
  if(num==2||num==3)
    return true;
  for(int i=sqrt(num+1)+1 ; i>=2 ; i--)
    if(num%i==0)
      return false;
  return true;
}

int main(){
  long int numToBeDiv=600851475143, largestPrimeDivisor;
  for(long int i=2 ; i<sqrt(600851475143) ; i++){
    if(isPrime(i) && numToBeDiv%i==0){
      largestPrimeDivisor=i;
      numToBeDiv=numToBeDiv/i;
      printf("%ld\t",i);
    }
  }
  printf("%ld\n",largestPrimeDivisor);
}
