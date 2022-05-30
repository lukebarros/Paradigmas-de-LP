#include<stdio.h>
int main(){
    int w = 168, x = 1, n1, n2, res, div;
    n1 = 2 * x;
    n2 = 3 * x;
    res = n1 + n2 - x;
    div = w/res;
    printf("%d", div);
    return 0;
}

