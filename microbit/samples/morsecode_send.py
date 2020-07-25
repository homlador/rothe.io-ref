from microbit import *
import radio
radio.on()
letter = ''
radio.config(length=251, group=31)
last_letter = ''
gfhj = ''
message = ''

a_start = -1
b_start = -1
separation = 700

def start(abc):
    global last_letter
    global gfhj
    global letter
    global message
    gfhj = ''
    if len(abc) < 5 and len(abc) > 0:
        if abc[0] == 's':
            if len(abc) == 1:
                gfhj = 'E'
                last_letter = 'E'
            elif abc[1] == 's':
                if len(abc) == 2:
                    gfhj = 'I'
                elif abc[2] == 's':
                    if len(abc) == 3:
                        gfhj = 'S'
                    elif abc[3] == 's':
                        gfhj = 'H'
                    elif abc[3] == 'l':
                        gfhj = 'V'
                elif abc[2] == 'l':
                    if len(abc) == 3:
                        gfhj = 'U'
                    elif abc[3] == 's':
                        gfhj = 'F'
            elif abc[1] == 'l':
                if len(abc) == 2:
                    gfhj = 'A'
                elif abc[2] == 's':
                    if len(abc) == 3:
                        gfhj = 'R'
                    elif abc[3] == 's':
                        gfhj = 'L'
                elif abc[2] == 'l':
                    if len(abc) == 3:
                        gfhj = 'W'
                    elif abc[3] == 's':
                        gfhj = 'P'
                    elif abc[3] == 'l':
                        gfhj = 'J'
        elif abc[0] == 'l':
            if len(abc) == 1:
                gfhj = 'T'
            elif abc[1] == 's':
                if len(abc) == 2:
                    gfhj = 'N'
                elif abc[2] == 's':
                    if len(abc) == 3:
                        gfhj = 'D'
                    elif abc[3] == 's':
                        if len(abc) == 4:
                            gfhj = 'B'
                        else:
                            gfhj = '  '
                    elif abc[3] == 'l':
                        gfhj = 'X'
                elif abc[2] == 'l':
                    if len(abc) == 3:
                        gfhj = 'K'
                    elif abc[3] == 's':
                        gfhj = 'C'
                    elif abc[3] == 'l':
                        gfhj = 'Y'
            elif abc[1] == 'l':
                if len(abc) == 2:
                    gfhj = 'M'
                elif abc[2] == 's':
                    if len(abc) == 3:
                        gfhj = 'G'
                    elif abc[3] == 's':
                        gfhj = 'Z'
                    elif abc[3] == 'l':
                        gfhj = 'Q'
                elif abc[2] == 'l':
                    if len(abc) >= 4:
                        display.scroll('falsch')
                        last_letter = ''
                        letter = ''
                        message = ''
                    else:
                        gfhj = 'O'
    elif abc == 'lsssl':
        gfhj = ' '
    else:
        display.scroll('falsch')
        last_letter = ''
        letter = ''
        message = ''


while True:
    if button_b.is_pressed():
        if b_start == -1:
            b_start = running_time()
        else:
            duration_b = running_time() - b_start
            if duration_b >= separation:
                display.show(Image.SQUARE)
    else:
        if b_start != -1:
            duration_b = running_time() - b_start
            b_start = -1
            display.clear()
            if duration_b >= separation:
                radio.send(letter)
                letter = ''
                last_letter = ''
                message = ''
                display.show(Image.YES, delay=200, wait=True, clear=True)
            else:
                letter = letter + 'e'
                start(last_letter)
                message = message + gfhj
                gfhj = ''
                display.scroll(message)
                last_letter = ''
    if button_a.is_pressed():
        if a_start == -1:
            a_start = running_time()
        else:
            duration_a = running_time() - a_start
            if duration_a >= separation:
                display.show(Image.SQUARE)
    else:
        if a_start != -1:
            duration_a = running_time() - a_start
            a_start = -1
            display.clear()
            if duration_a >= separation:
                letter = letter + 'l'
                last_letter = last_letter + 'l'
            else:
                letter = letter + 's'
                last_letter = last_letter + 's'