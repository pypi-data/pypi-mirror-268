def enumerate_print(src: str) -> None:
    for i, c in enumerate(src):
        if c != ' ':
            print('idx【{0}】,item【{1}】'.format(i, c))


if __name__ == '__main__':
    print('__main__'.title())
    t2cDict: dict = {}
    for idx, item in enumerate("Hello World!"):
        if item != ' ':
            t2cDict['[{0}:{1}]'.format(idx, idx + 1)] = "#111111"


    print(t2cDict)
    print("🔆🔅💯💹📈📉")

    s = None

    print(isinstance(s, str))