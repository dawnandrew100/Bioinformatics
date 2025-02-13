#include <stdio.h>

int aa_counter(char *seq, int *nuc_counter, char values[]);

int main(){
    char aa[] = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC";

    int nucleotides[4] = {0, 0, 0, 0};
    char nuc_values[4] = {'A', 'C', 'G', 'T'};
    if(aa_counter(aa, nucleotides, nuc_values) != 0){
        printf("Only nucleotides can be counted!");
    }

    int size = sizeof(nucleotides)/sizeof(nucleotides[0]);
    for(int i=0;i<size;i++){ //Amino acid with count (pseudo-dictionary)
        printf("%c:%d ", nuc_values[i], nucleotides[i]);
    }
    printf("\n\n");
    for(int i=0;i<size;i++){ //Rosalind-friendly printout
        printf("%d ", nucleotides[i]);
    }
    printf("\n");
    return 0;
}

int aa_counter(char *seq, int *nuc_counter, char values[]){
    for(int i=0; seq[i]!='\0'; i++){
        if(seq[i] == values[0]){
            nuc_counter[0]++;
        } else if(seq[i] == values[1]) {
            nuc_counter[1]++;
        } else if(seq[i] == values[2]) {
            nuc_counter[2]++;
        } else if(seq[i] == values[3]) {
            nuc_counter[3]++;
        } else {
            return 1;
        }
    }
    return 0;
}
