from itertools import product

def main():
    symbols = "ABCDEFGHI"
    n = 3
    symbols = list(symbols)
    symbols.sort()
    with open('results.txt', 'w') as file:
        for permutation in product(symbols, repeat=n):
            file.write(f'{"".join(permutation)}\n')

if __name__ == "__main__":
    main()
