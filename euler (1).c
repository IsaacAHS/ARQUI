#include <stdio.h>
#include <stdlib.h>
#include <math.h>
double euler (int x)
{   double out;
    out = pow(1+1/(double)x,(double)x);
    return out;}
int main()
{
    int N = 10000000;
    //double vector[N];
    //double *vector = (double *)calloc(N,sizeof(double));
    double *vector = (double *)malloc(N*sizeof(double));
    for (int i = 1; i<N;i++)
    {
        vector[i-1] = euler(i);
        printf("%.20lf \n",vector[i-1]);
    }
    free (vector);
    return 0;
}
