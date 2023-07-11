try:
    input_string = input("Enter a string: ")
    word_to_find = input("Enter the word to find: ")
    word_to_replace = input("Enter the word to replace: ")

    if word_to_find in input_string:
        new_string = input_string.replace(word_to_find, word_to_replace)
        print("Modified string:", new_string)
    else:
        print("The word to find " + "'" + word_to_find + "'" + " was not found in the string.")
except Exception as e:
    print(e)
