#include<stdio.h>
int main(){
    int w, x = 1, n1, n2, num1, num2, num3;
    printf("Numero: ");
    scanf("%d", &w);
    n1 = x + 1;
    n2 = x + 1 + 1;
    num1 = (w - (x + n1))/n2;
    num2 = num1 + x;
    num3 = num2 + x;
    printf("n1: %d\nn2: %d\nn3: %d", num1, num2, num3);
    return 0;
}