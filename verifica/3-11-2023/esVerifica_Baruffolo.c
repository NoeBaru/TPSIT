#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define LUNG_RIGA 200
#define TOT 2200
#define TOT_ALUNNO 100

/*
Author: Noemi Baruffolo
date: 3/11/2023
es. verifica
text:

- senza parentesi quadre “[]“ (ad esclusione del secondo parametro funzione STRTOK)
- allocare in modo dinamico la struttura al massimo del numero delle righe del file (punto 3) o che occupi minor spazio possibile.

1)	Stampare il valore totale degli incassi e restituire se si è raggiunto il totale di 2,200 euro indicando in modo preciso le
possibili anomalie (Esempio: mancano 80 euro) (punti 3)

2)	Ricerca il vostro nome, salvarlo in una struttura (campi: Cognome, quota) e verificare se avete pagato tutto la quota.
Gestire questa parte utilizzando una sola riga della struct (punti 3.5)

Esempio:
02/10/23;Ansaldi;40	------>Ansaldi 100
06/11/23;Ansaldi;60

3)	Restituire un report che indichi la situazione di tutti gli studenti, aggiungere un semplice messaggio nella printf in caso di
anomalie (punti 3,5)

(simulazione printf della struct)	Ansaldi 100 Ciobanu 100
Prandi 60	DA CONTROLLARE
Pollicino 100
*/

typedef struct{
    char* alunno;
    int quota;
} Campi;

int contaAlunni(char nomeFile[]) {
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

void caricaCampi(Campi classe[], char* fileName, char* campo, char* riga, int dim) {
    FILE* fp;
    fp = fopen(fileName, "r");

    char* data = "";
    int k = 0;

    if(fp == NULL) {
        printf("Il file %s non esiste o e' vuoto!\n", fileName);
        exit(1);   
    }
    for (Campi *p = classe; p < classe + dim; p++) {

        fgets(riga, LUNG_RIGA, fp);
        campo = strtok (riga,";");

        campo = strtok (NULL,";");
        data = strdup(campo);

        campo = strtok (NULL,";");
        p->alunno = strdup(campo);

        campo = strtok (NULL,";");
        p->quota = atoi(campo);

        k++;
        data = "";
        }
        fclose(fp); //chiude il file
}

void controlloTot(int tot, int max){
    int diff = 0;
    if(tot == max){
        printf("Si è raggiunto il totale di 2,200 €");
    } else{
        diff = max - tot;
        printf("Mancano ancora %d € per arrivare al totale di 2,200 €", diff);
    }
}

void stampaTot(Campi classe[], int dim) {
    int tot = 0;
   for (Campi *k = classe; k < classe + dim; k++){
        tot += k->quota;
    }
    printf("Il totale e': %d", tot);
    controlloTot(tot, TOT);
}

int ordNonDisg2(Campi *classe, int dim, char cognome) {
    int nx = 0;
    int *k = 0;
    while(*k < dim + classe) {
        if(strcmp(cognome, k->alunno) == 1) {
            nx++;
            *k = classe;
        }else 
            *k += 1;
    }
    return *k; //posizione
}

void controlloQuota(Campi* classe, int pos, int max){
    int diff = 0;
        if(classe[pos].alunno == max){
            diff = max - classe[pos].quota;
            printf("Mancano ancora %d € per arrivare al totale di 100 €", diff);
        }else{
            printf("%s ha pagato la quota intera!", classe[pos].alunno);
        }
}

void stampaClasse(Campi* classe, int dim) {
   for (Campi *p = classe; p < classe + dim; p++){
        printf("\n%s %d", p->alunno, p->quota);
    }
}

int main(){
    char fileName[] = "4AROB_GITA.csv";
    int dim;
    char *cognome = "Baruffolo";
    dim = contaAlunni(fileName);
    Campi* classe;
    
    classe = (Campi*) malloc(dim * sizeof(classe));
    char riga[LUNG_RIGA];
    char* campo;
      
    caricaCampi(classe, fileName, campo, riga, dim);

    stampaTot(classe, dim); //1)

    int pos = ordNonDisg2(classe, dim, cognome); //2)
    controlloQuota(classe, pos, TOT_ALUNNO);

    stampaClasse(classe, dim); //3) ma manca il messaggio della diff di soldi mancanti e errori vari

    free(classe);

    return 0;
}