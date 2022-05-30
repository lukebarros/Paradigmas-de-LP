#include<stdio.h>

int main(){
    int n, s, sp;
    float p, t;
    printf("Número de pessoas: ");
    scanf("%d", &n);
    printf("Preço ingresso: ");
    scanf("%f", &p);
    printf("Número de sócios presentes: ");
    scanf("%d", &s);
    sp = p*s/2;
    t = n*p + sp;
    printf("%.2f reais", t);
    return 0;
}