def get_count(input_str):
    vowels = 0
    for let in input_str:
        if let == "a" or let == "e" or let == "o" or let == "i" or let == "u":
            vowels += 1

    return vowels