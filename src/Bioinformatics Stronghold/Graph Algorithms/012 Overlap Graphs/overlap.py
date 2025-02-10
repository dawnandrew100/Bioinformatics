def main():
    input_string = 'rosalind_grph.txt'
    fasta_input = fasta_file_parser(input_string)
    overlap_dict = sequence_overlap(fasta_input, 3)
    for key, values in overlap_dict.items():
        for value in values:
            print(key, value)

def fasta_file_parser(fasta: str)-> dict[str, str]:
    """
    :param fasta: raw fasta file
    :return: fasta parsed into name:sequence dictionary
    """
    with open(fasta, 'r') as file:
        temp = [x.strip() for x in file.readlines()]
    fast_index = [i for i, j in enumerate(temp) if ">" in j]
    if len(fast_index) == 1:
        return {temp[0]: "".join(temp[1:])}
    if len(fast_index) >= 2:
        fasta_dict = {}
        for i, temp_index in enumerate(fast_index[:-1]):
            fasta_dict[temp[temp_index].strip('>')] = "".join(temp[temp_index+1:fast_index[i+1]])
        fasta_dict[temp[fast_index[-1]].strip('>')] = "".join(temp[fast_index[-1]+1:])
        return fasta_dict
    raise RuntimeError("Failed to parse file due to improper fasta format")

def sequence_overlap(fasta_dict: dict[str, str], k: int) -> dict[str, list[str]]:
    """
    :param fasta_dict: parse dictionary of fasta value pairs with the key being the name and the value being the sequence
    :param k: threshold value to limit noise in graph due to weak matches
    :return: returns dictionary of each pair that has an overlap equal to or greater than the threshold
    """
    overlap = {}
    for sequence in fasta_dict:
        temp = fasta_dict.copy() #need to explicitly copy dictionary or else both variables point to same object
        del temp[sequence] #stops sequence from matching with itself
        temp_overlap = [x for x in temp if fasta_dict[x].startswith(fasta_dict[sequence][-k:])]
        if temp_overlap: #only add non-empty lists to dictionary
            overlap[sequence] = temp_overlap
    return overlap

if __name__ == "__main__":
    main()
