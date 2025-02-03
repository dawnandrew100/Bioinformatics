def main():
    with open('main.txt', 'r') as file:
        input_text = [x.strip() for x in file.readlines()]
    
    hamming_dist = sum(x != y for x, y in zip(input_text[0], input_text[1]))
    print(hamming_dist)

if __name__ == "__main__":
    main()
