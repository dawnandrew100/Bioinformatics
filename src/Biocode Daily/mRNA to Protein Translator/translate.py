from biobase.constants import CODON_TABLE

def main():
    tests = ["AUGGCUCCCUAA", "GGGAUGAAACCCUGA", "AUGUUUGGA"]
    # expected = ["Met,Ala,Pro", "Met,Lys,Pro", "Met,Phe,Gly"]
    expected = ["MAP", "MKP", "MFG"]

    for i, test in enumerate(tests):
        result = translate_mrna(test)
        print(f"{test} translates to {"".join(result)}: {"".join(result) == expected[i]}\n")


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

if __name__ == "__main__":
    main()
