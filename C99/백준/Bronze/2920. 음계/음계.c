#include <stdio.h>

int main(void){
    int scale[8] = {0,};
    int cnt = 0;

    for (int i = 0; i < 8; i++){
        scanf("%d",&scale[i]);
        if (i && scale[i-1] < scale[i]) cnt++;
    }

    if (cnt == 7) printf("ascending"); 
    else if (cnt == 0) printf("descending");
    else printf("mixed");

    return 0;
}