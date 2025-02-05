def main():
    pre_translation = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    post_translation = rna_translation(pre_translation)
    if post_translation:
        print(f"Pre translation:\n{pre_translation}\n\nPost translation:\n{post_translation}")

def rna_translation(rna: str)->str:
    codon_table = { "UUU":"F",    "CUU":"L", "AUU":"I", "GUU":"V",
                    "UUC":"F",    "CUC":"L", "AUC":"I", "GUC":"V",
                    "UUA":"L",    "CUA":"L", "AUA":"I", "GUA":"V",
                    "UUG":"L",    "CUG":"L", "AUG":"M", "GUG":"V",
                    "UCU":"S",    "CCU":"P", "ACU":"T", "GCU":"A",
                    "UCC":"S",    "CCC":"P", "ACC":"T", "GCC":"A",
                    "UCA":"S",    "CCA":"P", "ACA":"T", "GCA":"A",
                    "UCG":"S",    "CCG":"P", "ACG":"T", "GCG":"A",
                    "UAU":"Y",    "CAU":"H", "AAU":"N", "GAU":"D",
                    "UAC":"Y",    "CAC":"H", "AAC":"N", "GAC":"D",
                    "UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
                    "UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
                    "UGU":"C",    "CGU":"R", "AGU":"S", "GGU":"G",
                    "UGC":"C",    "CGC":"R", "AGC":"S", "GGC":"G",
                    "UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
                    "UGG":"W",    "CGG":"R", "AGG":"R", "GGG":"G" }
    translation = []
    for codon in range(0,len(rna),3):
        translated = rna[codon:codon+3]
        if translated not in codon_table:
            return None
        if codon_table[translated] == "Stop":
            return "".join(translation)
        translation.append(codon_table[translated])
    return "".join(translation)

if __name__ == "__main__":
    main()
