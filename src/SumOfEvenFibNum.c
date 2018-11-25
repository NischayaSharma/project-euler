#include "stdio.h"
int fibonacci(int num){
  if(num==0)
    return 0;
  if(num==1)
    return 1;
  return fibonacci(num-1)+fibonacci(num-2);
}
int main() {
  int i, fibonacciNum, sum=0;
  for(i=0 ; fibonacciNum<4000000 ; i++){
    fibonacciNum=fibonacci(i);
    if(fibonacciNum%2==0)
      sum+=fibonacciNum;
  }
  printf("%d\n",sum);
}
