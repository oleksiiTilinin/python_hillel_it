def filter_words(input_file, output_file, min_word_length):
    with open(input_file, 'r') as file:
        content = file.read()
        words = content.split()
        filtered_words = [word for word in words if len(word) >= min_word_length]
        new_content = ' '.join(filtered_words)

    with open(output_file, 'w') as new_file:
        new_file.write(new_content)


def count_words(input_file):
    with open(input_file, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)


if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = 'output.txt'
    min_word_length = 7

    filter_words(input_file, output_file, min_word_length)
    word_count = count_words(input_file)

    print(f"Total words: {word_count}")
