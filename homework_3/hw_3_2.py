try:
    input_string = input("Input string: ")
    input_symbol = input("Input search symbol: ")

    symbol_count = 0
    for char in input_string:
        if char == input_symbol:
            symbol_count += 1

    print(symbol_count)
except Exception as e:
    print(e)
