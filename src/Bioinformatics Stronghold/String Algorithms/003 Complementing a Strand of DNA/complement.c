#include <stdio.h>
#include <string.h>

//return value is whether function was successful
int complement(char *sequence, char *comp, int len); 

int main(){
    char *seq = "AAAACCCGGT";
    int length = strlen(seq);
    char complemented[length];
    int success = complement(seq, complemented, length);
    if(success == 0) printf("%s\n", complemented);
    if(success != 0) printf("Encountered an invalid character!\n");
    return 0;
}

//sequence = input sequence, comp = buffer for outputted complement
int complement(char *sequence, char *comp, int len){
    char replicated[len]; //temp char array
    for(int i=0;i<len;i++){
        if      (sequence[i] == 'A') replicated[i] = 'T';
        else if (sequence[i] == 'T') replicated[i] = 'A';
        else if (sequence[i] == 'C') replicated[i] = 'G';
        else if (sequence[i] == 'G') replicated[i] = 'C';
        else {
            return 1;
        }
    }
    int i = 0;
    int seqlen = len;
    // reverses string by filling target backwards from temp array
    while (seqlen > 0) comp[i++] = replicated[seqlen-- - 1];
    comp[i] = '\0'; //final null byte to terminate string
    return 0;
}
