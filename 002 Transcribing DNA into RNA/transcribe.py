def main():
    input_string = input()
    Solution = transcribe(input_string)
    print(f"{Solution = }")

def transcribe(input_text):
    return input_text.replace("T", "U")

if __name__ == "__main__":
    main()
