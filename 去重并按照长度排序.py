def sort_by_length(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        strings = infile.read().splitlines()
    sorted_strings = sorted(strings, key=len)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for string in sorted_strings:
            outfile.write(string + '\n')

    print(f"Strings have been sorted by length and saved to: {output_file}")

def main():
    input_file = "输入文件的路径.txt"  
    output_file = "输出文件的路径.txt"  
    sort_by_length(input_file, output_file)

if __name__ == "__main__":
    main()
