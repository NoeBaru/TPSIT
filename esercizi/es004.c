#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define DIM 10

/*
author: Noemi Baruffolo
date: 21/09/2023
es: 004
text: Scrivi un programma in linguaggio C che consenta all'utente di creare un array dinamico
di interi. Il programma dove avere una dimensione array specificata, usando la
funzione malloc per allocare in modo dinamico gli interi.
L’utente deve poter inserire valori interi, che verranno stampati. Assicurarsi di liberare la
memoria allocata dinamicamente utilizzando la funzione free alla fine del
programma per evitare perdite di memoria.
*/

void stampaVett(iint vett, int dim){
    printf("Valori inseriti:\n");

        for(int cont = 0; cont < dim; cont++) {
            printf("%d ", vett[cont]);
        }
    printf("\n");
}

int main(){
    int dim;
    int* vett;
    
    // Chiedi all'utente di specificare la dimensione dell'vett
    printf("Inserisci la dimensione dell'vett: ");
    scanf("%d", &dim);

    // Alloca dinamicamente memoria per l'vett di interi
    vett = (int*)malloc(n * sizeof(int));

    if (vett != NULL) {

        printf("Inserisci %d valori interi:\n", dim);
        for(int cont = 0; cont < dim; cont++) {
            scanf("%d", &vett[cont]);
        }

        stampaVett(vett, dim);

        // Libera la memoria allocata dinamicamente
        free(vett);
    }

    return 0;
}