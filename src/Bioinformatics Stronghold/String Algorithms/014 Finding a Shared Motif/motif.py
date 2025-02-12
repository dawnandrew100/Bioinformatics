def main():
    parsed = fasta_file_parser('main.txt')
    print(longest_common_substring(parsed))

def fasta_file_parser(fasta: str)-> list[str]:
    """
    :param fasta: raw fasta string
    :return: fasta parsed into name:sequence dictionary
    """
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
    raise RuntimeError("Failed to parse file due to improper fasta format")

def common_substrings(fasta: list[str]) -> list[str]:
    if not isinstance(fasta, list):
        raise TypeError("Common substrings only accepts lists")
    if len(fasta) != 2:
        raise ValueError("Common substrings only takes a list of two strings")
    start, end = 0, 1
    longest_list = []
    while True:
        if start >= len(fasta[1]):
            break
        if end >= len(fasta[1]):
            if fasta[1][start:] in fasta[0] and len(fasta[1][start:]) > 1:
                options = [fasta[1][start:i] for i in range(2, len(fasta[1])+1) if len(fasta[1][start:i]) >= 2]
                longest_list.extend(options)
            start += 1
            end = start+1
        if fasta[1][start:end] not in fasta[0]:
            option = fasta[1][start:end-1]
            if option and len(option) > 1:
                options = [option[:i] for i in range(2, len(option)+1) if len(option) >= 2]
                longest_list.extend(options)
            start += 1
            end = start+1
            continue
        end += 1
    return longest_list

def longest_common_substring(fasta: list[str]) -> list[str]:
    motifs = common_substrings([fasta[0], fasta[-1]])
    if not motifs:
        raise ValueError("No common motifs found")
    shared_motifs = []
    for motif in motifs:
        if all(motif in sequence for sequence in fasta):
            shared_motifs.append(motif)
    if not shared_motifs:
        raise ValueError("No common motifs found")
    longest = [x for x in shared_motifs if len(x) == len(max(shared_motifs, key=len))]
    return longest

if __name__ == "__main__":
    main()
