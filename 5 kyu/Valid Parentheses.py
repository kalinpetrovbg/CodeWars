def valid_parentheses(string):
    opens = 0
    for each in string:
        if each == "(":
            opens += 1
        if each == ")":
            if opens > 0:
                opens -= 1
            else:
                return False

    if opens > 0:
        return False
    return True


print(valid_parentheses("  ("))