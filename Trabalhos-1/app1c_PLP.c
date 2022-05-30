#include <stdio.h>
#include <time.h>
int main(){
    clock_t begin = clock();
    printf("Hello World");
    clock_t end = clock();
    float time_spent = ((float)(end - begin) / CLOCKS_PER_SEC);
    printf("\nTempo de execução: %.2f ms", time_spent);
}