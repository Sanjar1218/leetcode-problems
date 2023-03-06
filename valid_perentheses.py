def is_valid(s: str) -> bool:
    last = s
    while s:
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
        if last == s:
            break
        last = s
    return len(s) == 0

if __name__ == '__main__':
    print(is_valid('()'))
    print(is_valid('()[]{}'))
    print(is_valid('(]'))
    print(is_valid('([)]'))
    print(is_valid('{[]}'))