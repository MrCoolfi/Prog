from lab10_package import lab7,lab8,lab9
import typer

def main(module: str, arg):
    match module:
        case '7': print(lab7.split(arg))
        case '8': print(lab8.f3(arg))
        case '9': print(lab9.f1(arg))
        case _: print(f"Неизвестный модуль: {module}")


if __name__ == "__main__":
    print("Запускающий модуль")
    typer.run(main)