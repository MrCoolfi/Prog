import lab7, lab8, lab9
import typer

# параметр arg может содержать исключительно строки, т.к. передается через аргументы коммандной строки, поэтому 7 и 9 не могут нормально работать. Это можно исправить, предварительно eval код, но это не безопасно.
def main(module: str, arg):
    match module:
        case '7': print(lab7.f1(arg))
        case '8': print(lab8.f2(arg))
        case '9': print(lab9.cat_data)
        case _: print(f"Неизвестный модуль: {module}")


if __name__ == "__main__":
    print("Запускающий модуль")
    typer.run(main)