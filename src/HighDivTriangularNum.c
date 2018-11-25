#include "stdio.h"
#include "math.h"

int thTriangularNum(int n){
  return (n*(n+1))/2;
}
int numOfFactors(int num){
  int counter=0;
  for(int i=1 ; i<=sqrt(num) ; i++){
    if(num%i==0)
      counter+=2;
  }
  if (sqrt(num)*sqrt(num)==num)
    counter--;
  return counter;
}

int main(){
  int i;
  for(i=1 ;; i++){
    if(numOfFactors(thTriangularNum(i))>=500)
      break;
  }
  printf("%d\t%d\n", thTriangularNum(i), i);
}
