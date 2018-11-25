#include "stdio.h"
#include "math.h"

int main(){
  int notPrime,count=0;
  for(int i=2 ;; i++)
  {
    notPrime=0;
    for(int j=sqrt(i+1) ; j>=2 ; j--)
      if(i%j==0) {
        notPrime=1;
        break;
      }
    if(notPrime==0)
      count++;
    if(count==10001){
      printf("%d\n",i);
      break;
    }
  }
}
