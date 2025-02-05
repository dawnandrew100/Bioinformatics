import re

def main():
    input_string = "GATATATGCATATACTT"
    input_pattern = "ATAT"
    result = find_substring_indexes(input_string, input_pattern)
    rosalind_result = [str(x) for x in result]
    print(" ".join(rosalind_result))

def find_substring_indexes(string: str, pattern: str, overlap: bool = True) -> list[int]:
    """
    :param string: text which contains substring
    :param pattern: substring to be found within string
    :return: list of positions (index + 1) of all occurences of pattern
    """
    if not overlap:
        #re.finditer finds non-overlapping matches
        return [m.start()+1 for m in re.finditer(f"{pattern}", string)]
    #putting pattern into a look-ahead capture group allows overlapping matches to be found
    #due to the look-ahead matching a zero-width substring in front of the pattern
    return [m.start()+1 for m in re.finditer(f"(?={pattern})", string)]

if __name__ == "__main__":
    main()
