def main():
    input_string = input()
    solution = dna_complement(input_string)
    print(f"Input:\n{input_string}\r\n\r\nSolution:\n{solution}")

def dna_complement(input_text):
    replacements = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join([replacements[x] for x in input_text[::-1]])

if __name__ == "__main__":
    main()
