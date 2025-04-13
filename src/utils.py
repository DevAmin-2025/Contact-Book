"""
Provide different and colorful ways to print texts.
"""
from termcolor import colored


def print_success(text):
    print(colored(text, 'green', attrs=['reverse']))


def print_info(text):
    print(colored(text, 'white', attrs=['reverse']))


def print_options(text):
    print(colored(text, 'white'))
