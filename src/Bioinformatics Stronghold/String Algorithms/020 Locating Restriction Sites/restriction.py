def main():
    input_seq = 'TCAATGCATGCGGGTCTATATGCAT'
    for location, sequence in find_restriction_sites(input_seq):
        print(location, len(sequence)) #can add restriction sequence to print statement if desired

def find_restriction_sites(input_string: str) -> list[tuple[int, str]]:
    sites = []
    for i, _ in enumerate(input_string):
        temp_search = input_string[i:i+12] # searching for up to 12 characters
        for j in range(2, 7):
            # compares first 2-6 chars to reverse complement of last 2-6 chars
            reverse = reverse_complement(temp_search[:j])
            if reverse == temp_search[j:j+j]: 
                # restriction site found if reverse complement of first half matches last half
                sites.append((i+1, temp_search[:j+j]))
    return sites

def reverse_complement(input_string:str) -> str | None:
    dna = "ACGT"
    if any(aa not in dna for aa in input_string):
        return None
    translation_table = str.maketrans(dna, dna[::-1])
    return input_string.translate(translation_table)[::-1]
if __name__ == "__main__":
    main()
