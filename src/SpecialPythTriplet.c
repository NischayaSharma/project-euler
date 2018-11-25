#include <stdio.h>

int isPythTriplet(int a, int b, int c){
  return ((a*a)+(b*b)==(c*c))? 1:0;
}

int main(){
  for(int i=0 ; i<=1000 ; i++)
    for(int j=0 ; j<=1000 ; j++)
      for(int k=0 ; k<=1000 ; k++)
        if(isPythTriplet(i,j,k) && i+j+k==1000)
          printf("%d\n",i*j*k);
}
