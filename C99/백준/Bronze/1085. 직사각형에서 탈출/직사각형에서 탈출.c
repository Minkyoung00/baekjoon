#include <stdio.h>

int main(){
    int x,y,w,h;
    scanf("%d %d %d %d", &x, &y, &w, &h);

    int min;

    min = x < w-x ? x : w-x;
    min = y < min ? y : min;
    min = h-y < min ? h-y : min; 

    printf("%d", min);
    
    return 0;
}