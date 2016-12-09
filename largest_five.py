def solution(digits):
    digits = sorted(list(digits), reverse=True)
    if len(digits) <= 5:
        return int("".join(map(str, digits)))
    else:
        return int("".join(map(str, digits))[0:5])
