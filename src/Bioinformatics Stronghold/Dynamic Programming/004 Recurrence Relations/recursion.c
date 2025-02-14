#include <stdio.h>

int rabbit_recur(int months, int offspring);

int main(){
    int n = 32;
    int k = 3;
    int rabbit = rabbit_recur(n, k);
    printf("%d\n", rabbit);
    return 0;
}

int rabbit_recur(int months, int offspring){
    if(months <= 0) return 0;
    if(months == 1) return 1;
    return rabbit_recur(months-1, offspring)+(rabbit_recur(months-2, offspring)*offspring);
}
