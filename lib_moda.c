char moda_c(char *array, int N){
    char contador_global=0;
    char contador_interno;
    char valor_retorno;
    for(int i=0; i<N; i++){
        contador_interno=0;
        for(int j=0; j<N; j++){
            if (array[j] == array[i]){
                contador_interno++;
            }
        }
        if (contador_interno>contador_global){
            contador_global=contador_interno;
            valor_retorno= array[i];
        }
    }
    return valor_retorno;
}