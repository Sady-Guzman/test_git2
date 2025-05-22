GranEntero *multiplicaGranEntero(GranEntero *resultado, GranEntero *a, GranEntero *b) {
    if (!resultado || !a || !b) return NULL;
    inicializar_GranEntero(resultado);

    int tamA = a->cantidad_Digitos;
    int tamB = b->cantidad_Digitos;
    int tamR = tamA + tamB;

    int *producto = calloc(tamR, sizeof(int));
    if (!producto) return NULL;

    // Copia dígitos de a y b en arreglos para acceso directo
    char *digA = malloc(tamA * sizeof(char));
    char *digB = malloc(tamB * sizeof(char));
    if (!digA || !digB) {
        free(producto);
        free(digA);
        free(digB);
        return NULL;
    }

    Nodo *na = a->digitos->primero;
    for (int i = 0; i < tamA && na; i++) {
        digA[i] = na->numero;
        na = na->siguiente;
    }
    Nodo *nb = b->digitos->primero;
    for (int i = 0; i < tamB && nb; i++) {
        digB[i] = nb->numero;
        nb = nb->siguiente;
    }

    // Multiplica
    for (int i = tamA - 1; i >= 0; i--) {
        for (int j = tamB - 1; j >= 0; j--) {
            int pos = i + j + 1;
            producto[pos] += (digA[i]) * (digB[j]);
        }
    }

    // Manejo de posicionamiento (acarreo)
    for (int i = tamR - 1; i > 0; i--) {
        producto[i - 1] += producto[i] / 10;
        producto[i] %= 10;
    }

    // Elimina ceros a la izquierda
    int inicio = 0;
    while (inicio < tamR - 1 && producto[inicio] == 0) {
        inicio++;
    }

    // Inserta dígitos en resultado, recorriendo desde inicio hasta fin
    for (int i = inicio; i < tamR; i++) {
        // Inserta
 al final usando tu función que añade nodo al final
        insertar_final(resultado->digitos, (char)producto[i]);
        resultado->cantidad_Digitos++;
    }

    // Determinar signo
    resultado->signo = (a->signo == b->signo) ? +1 : -1;

    // Liberar memoria temporal
    free(producto);
    free(digA);
    free(digB);

    return resultado;
}
