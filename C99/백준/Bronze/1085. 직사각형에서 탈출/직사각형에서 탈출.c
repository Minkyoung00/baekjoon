#include <stdio.h>

int main(){
    int x, y, w, h;
    scanf("%d %d %d %d", &x, &y, &w, &h);

    int min;
    if (x < w-x) min = x;
    else min = w-x;

    if (y < min) min = y;
    if (h-y < min) min = h-y; 

    printf("%d", min);
    return 0;
}