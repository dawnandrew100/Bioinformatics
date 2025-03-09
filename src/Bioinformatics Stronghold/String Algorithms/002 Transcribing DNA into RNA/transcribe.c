#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *to_transcribe(char *seq);

int main() {
  char *aa = "GATGGAACTTGACTACGTAAATT";
  char *transcribed = to_transcribe(aa);
  if (transcribed) {
    printf("%s\n", transcribed);
    free(transcribed);
  }
  return 0;
}

char *to_transcribe(char *seq) {
  int length = strlen(seq);
  char *t_seq = (char *)malloc(length * sizeof(char));
  if (!t_seq) {
    return NULL;
  }
  for (int i = 0; seq[i] != '\0'; i++) {
    if (seq[i] == 'T') {
      t_seq[i] = 'U';
    } else {
      t_seq[i] = seq[i];
    }
  }
  return t_seq;
}
