def main():
    input_string = input()
    Solution = count_nuc(input_string)
    print(f"{Solution = }")

def count_nuc(input_text):
    text = input_text.upper()
    nuc_count_dict = {nuc: text.count(nuc) for nuc in ["A", "C", "G", "T"]}
    return nuc_count_dict

if __name__ == "__main__":
    main()
