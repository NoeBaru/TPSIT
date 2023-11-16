#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/*
author: Noemi Baruffolo
date: 29/10/2023
es: 005
text: creare una lista che contiene dei valori numerici inseriti in inout (con struttura autoreferenziale)
*/

typedef struct node{
    int valore;
    struct node* next;
} Node;

int main(){
    int n;
    Node* lista = NULL;
    Node* l;

    do{
        printf("Inserisci un numero o -1 per terminare:\n");
        scanf("%d", n);

        if(n >= 0){
            if(lista  == NULL){
                lista = (Node*) malloc(sizeof(Node));
                l = lista;
            } else{
                l->next = (Node*) malloc(sizeof(Node));
                l = l->next;
            }
            l->valore = n;
            l->next = NULL;
        }
    } while(n >= 0);
    
    l = lista;
    printf("Numeri inseriti: ");

    while(l != NULL){
        printf("%d - %p \n", l->valore, l->next);
        l = l->next;
    }
    printf("\n");
    return 0;
}