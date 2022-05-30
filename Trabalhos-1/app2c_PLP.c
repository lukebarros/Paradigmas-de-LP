#include <stdio.h>
#include <time.h>
int main(){
    clock_t begin = clock();
    for (int i = 0;i <= 1000; i++){
        printf("%d\n",i);
    }
    clock_t end = clock();
    float time_spent = ((float)(end - begin) / CLOCKS_PER_SEC)*1000;
    printf("Tempo de execução: %.2f ms", time_spent);
    return 0;
}