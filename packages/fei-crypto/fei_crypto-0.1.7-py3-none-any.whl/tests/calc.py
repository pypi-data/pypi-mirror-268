if __name__ == '__main__':
    wide = True
    new_w = 299 if not wide else 28
    print(new_w)
    wide1: str | None = '123'
    if wide1 is not None and wide1 != '':
        print(wide1)
