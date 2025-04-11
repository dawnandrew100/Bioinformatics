def main():
    tests = ["GCGCGC", "AATTAA", "ATGCAT"]
    expected = ["GC-rich", "AT-rich", "AT-rich"]
    for i, test in enumerate(tests):
        result = classify_gc_content(test)
        print(f"{test} is {result}: {result == expected[i]}")

def classify_gc_content(dna: str) -> str:
    GC = dna.count('G') + dna.count('C')
    content = GC/len(dna)
    if content > 0.6:
        return "GC-rich"
    return "AT-rich"

if __name__ == "__main__":
    main()
