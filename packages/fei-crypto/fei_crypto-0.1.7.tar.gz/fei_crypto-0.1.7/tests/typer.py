import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


def basic(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    # print('typer.run')
    # typer.run(basic)
    print('app')
    app()
