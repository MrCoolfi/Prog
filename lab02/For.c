#include <stdio.h>
#include <math.h>

float f(float x, float h){
    const float eps = h/2;
    if (x > 0.0f - eps && x <= 1.5f + eps)
        return (pow(2,x) -2 + pow (x,2));
    else if (x > 1.5f - eps &&  x <= 3.0f + eps)
        return (sqrt(x) * exp(pow(-x,2)));
    return 0.0f;
}

int main()
{
    float h;
    printf ("Введите h "); scanf("%f", &h);
    printf("x\t\tf(x)\n");
    for(float x = 0; x <= 3.0f; x += h)
        printf("%f\t%f\n", x+h, f(x,h));
    return 0;
}