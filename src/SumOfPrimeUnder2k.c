#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool isPrime(int num){
  if(num==2||num==3)
    return true;
  for(int i=sqrt(num+1)+1 ; i>=2 ; i--)
    if(num%i==0)
      return false;
  return true;
}

int main(){
  int notPrime=0;
  long int sum=0;
  for(int i=2 ; i<=2000000 ; i++){
    if(isPrime(i))
      sum+=i;
  }
  printf("%ld\n",sum);
}
