#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/*
author: Noemi Baruffolo
date: 12/01/2024
es: 011
text: data in input una stringa e usando una pila, verificare se è palindroma o no
*/

typedef struct node{
    char valore;
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

    for(int cont = 0; head[cont] != '\n'; cont++){
        printf("%c ", l->valore[cont]);
        l = l ->next;
    }
}

int main() {
    int dim;
    char* str;
    Node* head = NULL;
    
    printf("inserire una parola: ");
    fflush(stdin);
    scanf("%s", str);
    if(str != NULL){
        Node* element = (Node*) malloc(sizeof(Node));
        for(int cont = 0; str[cont] != '\n'; cont++){
            element->valore = str[cont];
            push(&head, element);
        }
    }

    stampaPila(head);

    printf("\nFaccio la pop:\n");
    Node*  removed = pop(&head);
    printf("%c\n", removed->valore);

    stampaPila(head);
    
    return 0;
}