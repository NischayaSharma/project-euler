#include "stdio.h"
#include "math.h"

int main(){
  double num=pow(2,1000);
  int sum=0;
  printf("%lf\n",num);
  while (num>0){
    sum += (int)num%10;
    num = (int)num/10;
    printf("%lf\n",num);
  }
  printf("%d\n",sum);
}
