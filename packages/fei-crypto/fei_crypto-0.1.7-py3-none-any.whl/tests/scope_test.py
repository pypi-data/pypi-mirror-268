data = 'abc'


def print_data():
    global data
    data = '123'
    print(data)


if __name__ == '__main__':

    print_data()
    print(data)
