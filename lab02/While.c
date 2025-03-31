#include <stdio.h>
#include <math.h>

float f(float x, float h){
    const float eps = h/2;
    if (x > 0.0f - eps && x <= 1.5f + eps)
        return (pow(2,x) -2 + pow (x,2));
    else if (x > 1.5f + eps &&  x <= 3.0f + eps)
        return (sqrt(x) * exp(pow(-x,2)));
    return 0.0f;
}

int main()
{
    float h, x = 0;
    printf("Введите шаг -> "); scanf("%f", &h);
    printf("x\t\tf(x)\n");
    while(x <= 3.0f) {
        printf("%f\t%f\n", x+h, f(x,h));
        x += h;
    }
    return 0;

}