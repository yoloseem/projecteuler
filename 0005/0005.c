#include <stdio.h>
#include <math.h>

int main(void) {
    int factors[21] = {0,};

    int i, j, k, n;
    for(i=2; i<=20; i++) {
        n = i;
        for(j=2; j<=(int)sqrt(n); j++) {
            k = 0;
            while (n % j == 0) {
                n /= j;
                k++;
            }
            if (factors[j] < k) factors[j] = k;
        }
        if (n > 1 && !factors[n]) factors[n] = 1;
    }

    int result = 1;
    for (i=2; i<=20; i++) {
        for (j=0; j<factors[i]; j++)
            result *= i;
    }
    printf("%d\n", result);

    return 0;
}
