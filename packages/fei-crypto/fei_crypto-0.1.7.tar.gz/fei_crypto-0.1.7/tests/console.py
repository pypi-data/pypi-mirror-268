import os

from rich import console, traceback

con = console.Console()

if __name__ == '__main__':
    con.print(
        f"tg forward has a newer release v1.0.1 availaible!\
                \nVisit http://feicrypto.top",
        style="bold yellow",
    )
    con.print(os.getcwd(), style="blue")
    con.print(os.listdir(), style="green")
