#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/*
author: Noemi Baruffolo
date: 24/11/2023
es: 007
text:
Si consideri una lista dinamica di interi, i cui elementi sono del tipo definito come di seguito riportato:

typedef struct El {
    int dato;
    struct El *next;
} ELEMENTO;

• Si codifichi in C la funzione somma avente il seguente prototipo:

 int somma(ELEMENTO *Testa, int M)

• Tale funzione riceve come parametro la testa della lista e un intero M.

Quindi, restituisce la somma dei soli valori della lista che sono multipli di M. Se la lista è vuota, la funzione restituisce il valore -1.
*/

//quindi prendo m (tipo 3) lo metto in cima, poi sommo e quindi diventa 3 6 9 (ecc...)

typedef struct El{
    int dato;
    struct El *next;
} Elemento;

int main(){
    int m;
    Elemento* lista = NULL;
    Elemento* l;
    do{
        printf("Inserisci un naturale o -1 per terminare\n");
        scanf("%d",&m);
        if (m >= 0){
            if (lista == NULL){ /* prima iterazione */
                lista = (Elemento*) malloc(sizeof(Elemento));
                l = lista;
            }
            else{ /* iterazioni successive */
                l->next = (Elemento*) malloc(sizeof(Elemento));
                l = l->next;
            }

            l->dato = m;
            l->next = NULL;
        }
    } while (m >= 0);
    l = lista;
    printf("numeri inseriti: ");
    while (l != NULL){
        printf("%d - %p \n",l->dato, l->next);
        l = l->next;
    }
    printf("\n");
    return 0;
}
