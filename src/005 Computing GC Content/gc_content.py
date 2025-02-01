def main():
    dna_dict = fasta_file_parser('main.txt')
    print(highest_gc_content(dna_dict, is_rounded=True, places=6))

def fasta_file_parser(fasta: str)-> dict[str, str] | None:
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
    return None

def gc_content(input_string: str) -> float:
    gc = input_string.count("G") + input_string.count("C")
    return gc/len(input_string)*100

def highest_gc_content(gc_dict: dict[str, str] | None, is_rounded: bool = False, places: int = 2) -> str:
    if not gc_dict:
        return 'No fasta data to parse'

    dna_high_gc, highest_percent = "", 0
    for dna in gc_dict:
        gc_percent = gc_content(gc_dict[dna])
        if gc_percent > highest_percent:
            dna_high_gc = dna
            highest_percent = gc_percent
    if is_rounded:
        highest_percent = round(highest_percent, places)
    return f'{dna_high_gc}\n{highest_percent}'

if __name__ == "__main__":
    main()
