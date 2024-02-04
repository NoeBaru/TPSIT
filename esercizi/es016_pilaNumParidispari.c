#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/*
author: Noemi Baruffolo
date: 26/01/2024
es: 016 pila numeri interni pari e poi dispari
text: Considerate una sequenza di interi letti da input e definite una funzione C che li stampa
in modo tale che tutti i pari precedono i dispari, nello stesso ordine in cui vengono letti.
Ad esempio, se la sequenza è:
1 , 20 , 35 , 40 , 62 , 51 , 66
La stampa che si vuole ottenere e'
20 , 40 , 62 , 66 , 1 , 35 , 51
La funzione deve utilizzare come struttura dati di appoggio una pila o una coda.
*/

typedef struct node{
    int valore;
    struct node* next;
} Node;

int is_empty(Node* head){
    if(head == NULL){
        return 1;
    } else{
        return 0;
    }
}

void push(Node** head, Node* element){
    if(is_empty(*head)){
        *head = element;
        element->next = NULL;
    } else{
        element->next = *head;
        *head = element;
    }
}

Node* pop(Node** head){
    Node* ret = *head;
    if(is_empty(*head)){
        return NULL;
    } else{
        *head = ret->next;
    }
    return ret;
}

void stampaPila(Node* head){
    Node* l = head;
    printf("\nValori lista: ");
    while (l != NULL){
        printf("%d ", l->valore);
        l = l ->next;
    }
}

int main(){
    int n;
    Node* head = NULL;

    do{
        printf("inserire un numero naturale o -1 per terminare: ");
        scanf("%d", &n);
        if(n >= 0){
            Node* element = (Node*) malloc(sizeof(Node));
            element->valore = n;
            push(&head, element);
        }
    } while (n >= 0);

    stampaPila(head);

    printf("\nFaccio la pop:\n");
    Node*  removed = pop(&head);
    printf("%d\n", removed->valore);

    stampaPila(head);
    
    return 0;
}