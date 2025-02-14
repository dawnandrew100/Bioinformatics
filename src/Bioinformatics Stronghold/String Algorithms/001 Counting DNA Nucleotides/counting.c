#include <stdio.h>
#include <stdbool.h>

int aa_counter(char *seq, int *nuc_counter, char values[], int nuc_len);

int main(){
    char aa[] = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC";

    char nuc_values[] = {'A', 'C', 'G', 'T'};
    int size = sizeof(nuc_values)/sizeof(nuc_values[0]);
    int nucleotides[size] = {};
    if(aa_counter(aa, nucleotides, nuc_values, size) != 0){
        printf("Only nucleotides can be counted! Here are nucleotides counted before invalid char:\n");
    }
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

int aa_counter(char *seq, int *nuc_counter, char values[], int nuc_len){
    for(int i=0; seq[i]!='\0'; i++) {
        bool match = false;
        for(int j=0; j<nuc_len; j++) {
            if(seq[i] == values[j]) {
            nuc_counter[j]++;
            match = true;
            }
        }
        if (match == false) {
            return 1;
            }
    }
    return 0;
}
