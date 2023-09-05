#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    int n = 5; // Número de elementos

    // Asignar memoria para n enteros e inicializar a cero
    ptr = (int *)calloc(n, sizeof(int));

    if (ptr == NULL) {
        printf("No se pudo asignar memoria\n");
        return 1;
    }

    // Como se inicializó a cero, no es necesario establecer valores

    // Liberar la memoria asignada
    free(ptr);

    return 0;
}

