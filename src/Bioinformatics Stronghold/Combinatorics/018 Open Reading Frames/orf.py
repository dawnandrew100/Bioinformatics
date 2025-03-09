def main():
    input_fasta = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
    input_seq, rev_input_seq = parse_input(input_fasta)

    CODONS =  {"UUU":"F",    "UCU":"S",    "UAU":"Y",    "UGU":"C",
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

    forward = None
    reverse = None
    if input_seq is not None and rev_input_seq is not None:
        forward = orf_reader(input_seq, CODONS)
        reverse = orf_reader(rev_input_seq, CODONS)

    all_orfs = None
    if forward is not None and reverse is not None:
        all_orfs = forward.union(reverse)

    if all_orfs == None:
        all_orfs = forward if forward is not None else reverse

    if all_orfs is not None:
        for orf in all_orfs:
            print(orf)

    if all_orfs == None:
        print("No open reading frames present in input sequence")

def parse_input(input_seq: str) -> tuple[str | None, ...]:
    input_seq = input_seq.replace('T', 'U')
    rev_input_seq = reverse_complement(input_seq)
    if input_seq == None or rev_input_seq == None:
        return None, None
    return input_seq, rev_input_seq


def reverse_complement(input_string:str) -> str | None:
    complement = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    if any(aa not in complement for aa in input_string):
        return None
    return "".join(complement[base] for base in input_string[::-1])

def orf_reader(input_string: str, CODON_TABLE: dict[str, str]) -> set[str] | None:
    if len(input_string) < 3:
        return None

    start = 0
    end = start + 3
    orfs = set()
    for _ in range(len(input_string)):
        if end >= len(input_string)-1:
            break
        aa = CODON_TABLE[input_string[start:end]]
        if aa == 'M':
            temp_orf = []
            temp_start = start
            temp_end = end
            while aa != 'STOP' and temp_end <= len(input_string):
                aa = CODON_TABLE[input_string[temp_start:temp_end]]
                temp_orf.append(aa)
                temp_start += 3
                temp_end += 3
            if 'STOP' not in temp_orf:
                continue
            orfs.add("".join(temp_orf[:-1]))
        start += 1
        end += 1

    if len(orfs) == 0:
        return None
    return orfs

if __name__ == "__main__":
    main()
