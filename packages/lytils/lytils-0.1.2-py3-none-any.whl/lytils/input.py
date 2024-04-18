# Standard Libraries
import msvcrt
import time

# Local Libraries
from .print import cprint, ctext

def cinput(text, level = 0):
    str_level = ""
    for _ in range(0, level):
        str_level += "  "
    
    return input(f"{str_level}{ctext(text)}")

def pause(text="Press <y><ENTER><w> to continue..."):
    return cinput(text)

def press_enter_or_wait_to_continue(seconds):
    t0 = time.time()
    cprint(f"Press <y><ENTER><w> or <y>wait {seconds} seconds<w>...")
    while time.time() - t0 < 300:
        if msvcrt.kbhit():
            if msvcrt.getch() == b'\r': # not '\n'
                break
        time.sleep(0.1)