from string import lowercase


def lowercase_count(strng):
    return len([char for char in strng if char in lowercase])
