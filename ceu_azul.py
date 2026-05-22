import time
import os
import sys
from rich.console import Console
from rich.live import Live
from rich.text import Text
from pyfiglet import Figlet

console = Console()


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def intro():

    limpar()

    fig = Figlet(font="slant")
    titulo = fig.renderText("Ceu Azul")

    console.print(f"[bold blue]{titulo}[/]")

    tamanho = 40

    for i in range(tamanho + 1):

        porcentagem = int((i / tamanho) * 100)

        barra = "━" * i
        vazio = "─" * (tamanho - i)

        sys.stdout.write(
            f"\r\033[1;34m{barra}\033[0m\033[37m{vazio}\033[0m "
            f"\033[1;37m{porcentagem}%\033[0m"
        )

        sys.stdout.flush()

        time.sleep(0.05)

    print("\n")
    console.print("[bold white]Sistema carregado...[/]")

    time.sleep(1.5)

    limpar()


def escrever(texto, velocidade=0.07, cor="white"):

    frase = ""

    with Live("", console=console, refresh_per_second=30, transient=True) as live:

        for letra in texto:

            frase += letra

            txt = Text(frase, style=f"bold {cor}")

            live.update(txt)

            time.sleep(velocidade)

    console.print(Text(texto, style=f"bold {cor}"))

    time.sleep(0.6)


def musica():

    escrever("A gente nunca sabe quem são essas pessoas", 0.06, "white")

    time.sleep(2)

    escrever("Eu só queria te lembrar", 0.09, "blue")

    console.print()

    time.sleep(2.7)

    escrever("Que aquele tempo, eu não podia fazer mais por nós", 0.07, "white")

    escrever("Eu estava errado e você não tem que me perdoar", 0.06, "blue")

    time.sleep(2)

    escrever("Mas também quero te mostrar", 0.08, "white")

    console.print()

    time.sleep(3)

    escrever("Que existe um lado bom nessa história", 0.09, "blue")

    escrever("Tudo o que ainda temos a compartilhar", 0.09, "white")

    console.print()

    escrever("E viver, e cantar", 0.12, "blue")

    time.sleep(2)


def main():

    intro()
    musica()


main()
