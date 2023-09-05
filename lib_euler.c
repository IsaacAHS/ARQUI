#include <math.h>

double euler (int x){
    double out;
    out = pow(1+1/(double)x,(double)x);
    return out;
}