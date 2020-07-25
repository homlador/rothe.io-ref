from microbit import *
import radio

radio.on()
radio.config(length=251, group=31)
def start(abc):
    if len(abc) < 1:
        return ''
    if abc[0] == 's':
        if len(abc) == 1:
            return 'E'
        elif abc[1] == 's':
            if len(abc) == 2:
                return 'I'
            elif abc[2] == 's':
                if len(abc) == 3:
                    return 'S'
                elif abc[3] == 's':
                    return 'H'
                elif abc[3] == 'l':
                    return 'V'
            elif abc[2] == 'l':
                if len(abc) == 3:
                    return 'U'
                elif abc[3] == 's':
                    return 'F'
        elif abc[1] == 'l':
            if len(abc) == 2:
                return 'A'
            elif abc[2] == 's':
                if len(abc) == 3:
                    return 'R'
                elif abc[3] == 's':
                    return 'L'
            elif abc[2] == 'l':
                if len(abc) == 3:
                    return 'W'
                elif abc[3] == 's':
                    return 'P'
                elif abc[3] == 'l':
                    return 'J'
    elif abc[0] == ('l'):
        if len(abc) == 1:
            return 'T'
        elif abc[1] == 's':
            if len(abc) == 2:
                return 'N'
            elif abc[2] == 's':
                if len(abc) == 3:
                    return 'D'
                elif abc[3] == 's':
                    if len(abc) == 4:
                        return 'B'
                    else:
                        return '  '
                elif abc[3] == 'l':
                    return 'X'
            elif abc[2] == 'l':
                if len(abc) == 3:
                    return 'K'
                elif abc[3] == 's':
                    return 'C'
                elif abc[3] == 'l':
                    return 'Y'
        elif abc[1] == 'l':
            if len(abc) == 2:
                return 'M'
            elif abc[2] == 's':
                if len(abc) == 3:
                    return 'G'
                elif abc[3] == 's':
                    return 'Z'
                elif abc[3] == 'l':
                    return 'Q'
            elif abc[2] == 'l':
                return 'O'
    return

while True:
    x = radio.receive()
    if x is not None:
        letters = x.split('e')
        y = 0
        abc = ''
        text = ''
        while y < len(letters):
            abc = letters[y]
            text = text + start(abc)
            y += 1
        display.scroll(text)