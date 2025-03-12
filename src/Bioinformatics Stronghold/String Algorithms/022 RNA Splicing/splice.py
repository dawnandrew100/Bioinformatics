def main():
    parsed = fasta_file_parser('rosalind_splc.txt')
    input_seq = parsed[0]
    introns = parsed[1:]
    exon_input_seq = input_seq
    protein = []

    for intron in introns:
        exon_input_seq = exon_input_seq.replace(intron, '') #remove introns

    exon_input_seq = exon_input_seq.replace('T', 'U') #dna -> rna
    for i in range(0, len(exon_input_seq), 3):
        translation = CODON_TABLE[exon_input_seq[i:i+3]] #codon -> amino acid
        if translation == "STOP":
            break
        protein.append(translation)

    print("".join(protein))

def fasta_file_parser(fasta: str)-> list[str]:
    with open(fasta, 'r') as file:
        temp = [x.strip() for x in file.readlines()]
    fast_index = [i for i, j in enumerate(temp) if ">" in j]
    if len(fast_index) == 1:
        return ["".join(temp[1:])]
    if len(fast_index) >= 2:
        fasta_dict = {}
        for i, temp_index in enumerate(fast_index[:-1]):
            fasta_dict[temp[temp_index].strip('>')] = "".join(temp[temp_index+1:fast_index[i+1]])
        fasta_dict[temp[fast_index[-1]].strip('>')] = "".join(temp[fast_index[-1]+1:])
        return list(fasta_dict.values())
    raise ValueError("Failed to parse file due to improper fasta format")

CODON_TABLE =  {"UUU":"F",    "UCU":"S",    "UAU":"Y",    "UGU":"C",
                "UUC":"F",    "UCC":"S",    "UAC":"Y",    "UGC":"C",
                "UUA":"L",    "UCA":"S",    "UAA":"STOP", "UGA":"STOP",
                "UUG":"L",    "UCG":"S",    "UAG":"STOP", "UGG":"W",
                "CUU":"L",    "CCU":"P",    "CAU":"H",    "CGU":"R",
                "CUC":"L",    "CCC":"P",    "CAC":"H",    "CGC":"R",
                "CUA":"L",    "CCA":"P",    "CAA":"Q",    "CGA":"R",
                "CUG":"L",    "CCG":"P",    "CAG":"Q",    "CGG":"R",
                "AUU":"I",    "ACU":"T",    "AAU":"N",    "AGU":"S",
                "AUC":"I",    "ACC":"T",    "AAC":"N",    "AGC":"S",
                "AUA":"I",    "ACA":"T",    "AAA":"K",    "AGA":"R",
                "AUG":"M",    "ACG":"T",    "AAG":"K",    "AGG":"R",
                "GUU":"V",    "GCU":"A",    "GAU":"D",    "GGU":"G",
                "GUC":"V",    "GCC":"A",    "GAC":"D",    "GGC":"G",
                "GUA":"V",    "GCA":"A",    "GAA":"E",    "GGA":"G",
                "GUG":"V",    "GCG":"A",    "GAG":"E",    "GGG":"G"}

if __name__ == "__main__":
    main()
