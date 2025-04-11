def main():
    tests = ["AUGGCUCCCUAA", "GGGAUGAAACCCUGA", "AUGUUUGGA"]
    expected = ["Met,Ala,Pro", "Met,Lys,Pro", "Met,Phe,Gly"]

    for i, test in enumerate(tests):
        result = translate_mrna(test)
        print(f"{test} translates to {expected[i]}: {result == expected[i].split(",")}\n")

def translate_mrna(mrna: str) -> list[str]:
    start = mrna.find("AUG")
    prot = []
    if start == -1:
        return prot
    for i in range(start, len(mrna), 3):
        aa = CODON_TABLE[mrna[i:i+3]]
        if aa == 'STOP':
            break
        prot.append(aa)
    return prot

# Will update CODON TABLE to use biobase when launched on PyPI
CODON_TABLE = { 'AUG': 'Met', 'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu', 'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', 'UAU': 'Tyr', 'UAC': 'Tyr', 'UGU': 'Cys', 'UGC': 'Cys', 'UGG': 'Trp', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu', 'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro', 'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln', 'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr', 'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys', 'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg', 'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val', 'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala', 'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu', 'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly', 'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP' }

if __name__ == "__main__":
    main()
