from typing import Tuple, Dict, Any

from pydantic.main import BaseModel


class TestCaption(BaseModel):
    check: bool = False
    header: str = ""
    footer: str = ""


class TestTuple(BaseModel):
    ok: bool = True
    caption: TestCaption = TestCaption()


class TestModel:
    id_ = "plugin"

    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = data


if __name__ == '__main__':
    def fun_a(a: Tuple[str, int]) -> Tuple:
        return a


    r = fun_a(('aa', 12))
    print(r)
    for item in TestTuple():
        print(type(item[1]))
        print(type(item))
        print(item)
        print('-' * 50)
        # print(item)
        # print(item[0], item[1])
        # print(type(item))

    tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    for item in tinydict:
        print(type(item))
        print(item)
        print('-' * 50)
