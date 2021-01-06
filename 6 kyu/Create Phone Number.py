def create_phone_number(n):
    result = ""
    for num in n:
        num = str(num)
        result += num
    return f"({result[:3]}) {result[3:6]}-{result[6:]}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
