def sort_by_length(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        strings = infile.read().splitlines()
    sorted_strings = sorted(strings, key=len)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for string in sorted_strings:
            outfile.write(string + '\n')

    print(f"Strings have been sorted by length and saved to: {output_file}")

def main():
    input_file = " 你放入的地方"
    output_file = "你想保存的地方"
    sort_by_length(input_file, output_file)
if __name__ == "__main__":
    main()
