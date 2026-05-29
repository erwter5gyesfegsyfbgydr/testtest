import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

def blue_to_white_gradient(text):
    lines = text.strip().split('\n')
    result = []
    num_lines = len(lines)
    
    for i, line in enumerate(lines):
        intensity = int(255 * (i / max(num_lines - 1, 1)))
        r = intensity
        g = intensity
        b = 255
        
        color = f"\033[38;2;{r};{g};{b}m"
        reset = "\033[0m"
        
        colored_line = color + line + reset
        result.append(colored_line)
    
    return '\n'.join(result)

banner = fr"""
▀█████████▄   ▄██████▄  ▄██   ▄      ▄█   ▄█▄  ▄█     ▄████████    ▄████████    ▄████████    ▄████████ 
  ███    ███ ███    ███ ███   ██▄   ███ ▄███▀ ███    ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    ███ ███    ███ ███▄▄▄███   ███▐██▀   ███▌   ███    █▀    ███    █▀    ███    █▀    ███    ███ 
 ▄███▄▄▄██▀  ███    ███ ▀▀▀▀▀▀███  ▄█████▀    ███▌   ███          ███         ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███▀▀▀██▄  ███    ███ ▄██   ███ ▀▀█████▄    ███▌ ▀███████████ ▀███████████ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ██▄ ███    ███ ███   ███   ███▐██▄   ███           ███          ███   ███    █▄  ▀███████████ 
  ███    ███ ███    ███ ███   ███   ███ ▀███▄ ███     ▄█    ███    ▄█    ███   ███    ███   ███    ███ 
▄█████████▀   ▀██████▀   ▀█████▀    ███   ▀█▀ █▀    ▄████████▀   ▄████████▀    ██████████   ███    ███ 
                                    ▀                                                       ███    ███ 
"""

print(blue_to_white_gradient(banner))
input("                     Enter >> ")
