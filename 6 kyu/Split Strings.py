from textwrap import wrap

def solution(s):
    result = wrap(s, 2)
    if len(s) % 2 != 0:
        z = result.pop()
        z += "_"
        result.append(z)
        return result
    return result


print(solution("abcd"))