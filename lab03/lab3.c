#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fill(int n, int a[])
{
    int i;
    for (i = 0; i < n; i++)
        a[i] = rand () % 101 - 50;
}

void lol(int n, int a[]){
    for (int i = 0; i<n; i++){
        for (int j = i+1; j<n; j++)
            if (a[i] == a[j]){
                int sum = 0;
                int proiz = 1;
                for (int k = i+1; k <j;k++){
                    sum += a[k];
                    proiz = proiz * a[k];
                }
                a[i] = sum;
                a[j] = proiz;
                break;
            }
    }
    
}


int main()
{
    srand(time(NULL));
    int n;
    printf("n -> ");
    scanf("%d", &n);
    int A[n];
    fill(n, A);
    int i;
    for (i = 0; i < n; i++)
        printf("%4d", A[i]);
    printf("\n");
    printf("Изменненый массив\n");
    lol(n,A);
    for (i = 0; i < n; i++)
        printf("%4d", A[i]);
    printf("\n");
    return 0;
}
