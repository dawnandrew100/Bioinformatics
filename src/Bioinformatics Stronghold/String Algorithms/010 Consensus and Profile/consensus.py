def main():
    text_dict, seq_len = fasta_file_parser('input.txt')
    nucs = ["A", "T", "C", "G"]
    index_to_ATCG, ATCG_to_index = create_nuc_dict(nucs)
    matrix = ATCG_matrix(text_dict.values(), ATCG_to_index, seq_len)
    consensus_seq_array = [position.index(max(position)) for position in matrix]
    consensus = [index_to_ATCG[nuc] for nuc in consensus_seq_array]
    print("".join(consensus))
    
def fasta_file_parser(fasta: str)-> tuple[dict[str, str], int]:
    with open(fasta, 'r') as file:
        temp = [x.strip() for x in file.readlines()]
    fast_index = [i for i, j in enumerate(temp) if ">" in j]
    if len(fast_index) == 1:
        return {temp[0]: "".join(temp[1:])}, len("".join(temp[1:]))
    if len(fast_index) >= 2:
        fasta_dict = {}
        for i, temp_index in enumerate(fast_index[:-1]):
            fasta_dict[temp[temp_index].strip('>')] = "".join(temp[temp_index+1:fast_index[i+1]])
        fasta_dict[temp[fast_index[-1]].strip('>')] = "".join(temp[fast_index[-1]+1:])
        return fasta_dict, len("".join(temp[fast_index[-1]+1:]))
    raise RuntimeError("Failed to parse file due to improper fasta format")

def create_nuc_dict(nucleotides: list[str]) -> tuple[dict[int, str], dict[str, int]]:
    indexed_nucleotides = dict(enumerate(nucleotides))
    nucleotide_dict = {nuc:i for i, nuc in enumerate(nucleotides)}
    return indexed_nucleotides, nucleotide_dict

def ATCG_matrix(text: list[str], ATCG_index: dict[str, int], length: int) -> list[list[int]]:
    matrix = [[0 for _ in range(4)] for _ in range(length)]
    for seq in text:
        for i, nuc in enumerate(seq):
            matrix[i][ATCG_index[nuc]] += 1
    return matrix

if __name__ == "__main__":
  main()
