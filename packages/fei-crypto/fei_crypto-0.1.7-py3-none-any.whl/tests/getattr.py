class A(object):
    bar = 1


if __name__ == '__main__':
    a = A()
    print(getattr(a, 'bar'))
    obj = getattr(a, 'bar2')
    if obj:
        print('ok')
    print('---------------------')
