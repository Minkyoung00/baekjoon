#include <stdio.h>

int main(void){
    int n, x, y;
    int Q1, Q2, Q3, Q4, AXIS;
    Q1 = Q2 = Q3 = Q4 = AXIS = 0;

    scanf("%d",&n);
    
    for (int i = 0; i < n; i++){
        scanf("%d %d",&x, &y);
        if (x == 0 || y == 0) AXIS++;
        else if(x > 0 && y > 0) Q1++;
        else if(x < 0 && y > 0) Q2++;
        else if(x < 0 && y < 0) Q3++;
        else if(x > 0 && y < 0) Q4++;
    }

    printf("Q1: %d\nQ2: %d\nQ3: %d\nQ4: %d\nAXIS: %d", Q1, Q2, Q3, Q4, AXIS);

    return 0;
}