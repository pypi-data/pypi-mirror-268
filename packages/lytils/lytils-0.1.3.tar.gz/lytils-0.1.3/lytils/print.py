import traceback

COLORS = {
    "white": '\033[0m', # default,
    "red": '\033[31m',
    "green": '\033[32m',
    "yellow": '\033[33m',
    "blue": '\033[34m',
    "magenta": '\033[35m',
    "cyan": '\033[36m'
}

def ctext(text):
    text = text.replace("<w>", COLORS['white'])
    text = text.replace("<r>", COLORS['red'])
    text = text.replace("<g>", COLORS['green'])
    text = text.replace("<y>", COLORS['yellow'])
    text = text.replace("<b>", COLORS['blue'])
    text = text.replace("<m>", COLORS['magenta'])
    text = text.replace("<c>", COLORS['cyan'])
    
    return f"{text}{COLORS['white']}"

def cprint(text, level = 0):
    text = ctext(text)

    str_level = ""
    for i in range(0, level):
        str_level += "  "
    
    print(f"{str_level}{text}{COLORS['white']}")

def print_trace(color='red'):
    set_print_color(color)
    traceback.print_exc()
    reset_print_color()

def reset_print_color():
    print(COLORS['white'])

def set_print_color(color):
    print(COLORS[color])