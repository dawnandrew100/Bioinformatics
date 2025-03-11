from itertools import permutations

def main():
    n = 7
    members = range(1, n+1)
    results = []
    for permutation in permutations(members):
        temp = [str(x) for x in permutation]
        results.append(" ".join(temp))

    with open("results.txt", "w") as file:
        file.write(f"{len(results)}\n")
        for result in results:
            file.write(f"{result}\n")

if __name__ == "__main__":
    main()
