import pyfiglet
from termcolor import colored


def welcome():
    print(
        colored("_______________________________________________________",
                'light_blue'))
    print("                                                    ")
    pyfiglet.print_figlet(text="Nstream AI ", colors="BLUE")
    print(
        colored("______________________________________________________",
                'light_blue'))
    print("                                                    ")
    print(colored("Copyright © 2024-25", 'dark_grey'))
    print("                                                    ")
    print("                                                    ")
    print("                                                    ")
    print(
        colored("A High Performance Stream Processor powered by Gen AI",
                'red'))
    print("                                                    ")
    print(colored("Dashboard at https://console.nstream.ai", 'light_cyan'))
    print("                                                    ")
    print("                                                    ")
    print("                                                    ")
