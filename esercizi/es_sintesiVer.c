#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define DIM 100
#define LIM_MIN 1
#define LIM_MAX 20
#define LUNG_RIGA 200
#define NOME_FILE "sintesi.csv"

/*
author: Noemi Baruffolo
date: 17/10/2023
es: sintesi
text:
-Creare un file .csv con COGNOME, NOME, NASCITA (annomesegiorno in formato INT)
-scorrere il file con la funzione FGETS e STRTOK
-stampare in ordine DECRESCENTE (dal più grande al più piccolo)
 utilizzando i puntatori e allocazione dinamica (MALLOC)
*/


typedef struct {
    char* cognome;
    char* nome; //char tittle[STRL];
    int data;
} Persona;

int contaPersone(char nomeFile[]) {
    int c;
    int cont = 0;

    FILE *fp;
    fp = fopen(nomeFile,"r");

    if(fp != NULL) {
        while ((c = fgetc(fp)) != EOF) {
            if(c =='\n') {
                cont++;
            }
        }
        fclose(fp); //chiude il file
    }
    return cont;
}

void caricaFile(Persona contatti[], char* fileName, char* campo, char* riga, int dim) {
    FILE* fp;
    fp = fopen(fileName, "r");
    int k = 0;

    if(fp == NULL) {
        printf("Il file %s non esiste o e' vuoto!\n", fileName);
        exit(1);   
    }
    for (int *p = contatti; p < contatti + dim; p++) {

        fgets(riga, LUNG_RIGA, fp);
        campo = strtok (riga,",");
        //(*(contatti + k)).number = atoi(campo); //più pesante e scomoda, meglio la seguente
        (contatti + k)->cognome = atoi(campo); //atoi passa da stringa e int con atof da stringa a float

        campo = strtok (NULL,",");
        (contatti + k)->nome = strdup(campo); //strdup duplica il campo

        campo = strtok (NULL,",");
        (contatti + k)->data = strdup(campo);

        k++;

        }
        fclose(fp); //chiude il file
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort3(Persona contatto, int n) {
    int k, sup, sca; 
    sup = n - 1;
    while (sup > 0) {
        sca = 0;
        for (k = 0; k < sup ; k++) {
            if ((contatto.data + k) > (contatto.data + k + 1)){
                swap((contatto.data + k), (contatto.data + k + 1));
                sca = k ;
            }
        }
        sup = sca ;
    }
}

void stampaPersona(Persona contatti[], int dim) {
   for (int *k = contatti; k < contatti + dim; k++){
        printf("\n%s %s %d", (contatti + (*k))->cognome, (contatti + (*k))->nome, (contatti + (*k))->data);
    }
}

int main(){
    int dim;
    dim = contaPersona(NOME_FILE);
    Persona* contatti;
    
    contatti = (Persona*) malloc(dim * sizeof(Persona));
    char riga[LUNG_RIGA];
    char* campo;
      
    caricaFile(contatti, NOME_FILE, campo, riga, dim);

    bubbleSort3(contatti, dim); //ordina il vettore

    stampaPersona(contatti, dim);

    return 0;
}