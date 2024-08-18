from art import text2art
from termcolor import colored
import random

def generate_ascii_art(text):
    ascii_art = text2art(text)
    colored_art = ""
    for line in ascii_art.split('\n'):
        color = random_color()
        colored_art += colored(line, color) + '\n'
    return colored_art

def random_color():
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    return random.choice(colors)
