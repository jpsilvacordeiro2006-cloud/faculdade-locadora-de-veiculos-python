import sys

from locadora import Locadora
from menu import Menu


def main():
    # para os acentos aparecerem certo no terminal do Windows
    sys.stdout.reconfigure(encoding="utf-8")

    locadora = Locadora()
    menu = Menu(locadora)
    menu.executar()


if __name__ == "__main__":
    main()
