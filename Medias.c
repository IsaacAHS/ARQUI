#include <stdio.h>
#include <math.h>
double MediaAritmetica(double *arr,int N){
    double suma=0.0;
    for(int i=0;i<N;i++){
        suma= arr[i]+suma;
    }
    return suma/N;
}

int main() {
    int n;
    printf("Ingrese el número de elementos: ");
    scanf("%d", &n);
    double arr[n];
    printf("Ingrese los elementos: ");
    // int n= atoi(argv[1]);
    
    for (int i = 0; i < n; i++) {
        scanf("%lf", &arr[i]);
    }
    double sum = 0, product = 1, harmonicSum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
        product *= arr[i];
        harmonicSum += 1 / arr[i];
    }
    double arithmeticMean = sum / n;
    double geometricMean = pow(product, 1.0 / n);
    double harmonicMean = n / harmonicSum;
    printf("Media aritmética: %lf\n", MediaAritmetica(arr,n));
    printf("Media geométrica: %lf\n", geometricMean);
    printf("Media armónica: %lf\n", harmonicMean);
    return 0;
}
