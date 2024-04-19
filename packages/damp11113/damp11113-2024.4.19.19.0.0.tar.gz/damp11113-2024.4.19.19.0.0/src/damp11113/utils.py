"""
damp11113-library - A Utils library and Easy to use. For more info visit https://github.com/damp11113/damp11113-library/wiki
Copyright (C) 2021-2024 damp11113 (MIT)

Visit https://github.com/damp11113/damp11113-library

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import math
import operator
import time, sys
from functools import reduce
from time import sleep
from datetime import datetime
from threading import Thread
from .randoms import rannum
from .file import removefile, readfile, writefile2, createfile
from inspect import getmembers, isfunction
import ctypes
from gtts import gTTS
from playsound import playsound
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from shutil import get_terminal_size
from decimal import Decimal, getcontext

def grade(number):
    score = int(number)
    if score == 100:
        return "Perfect"
    elif score >= 100:
        return '0 - 100 only'
    elif score >= 95:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 75:
        return "C+"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D+"
    elif score >= 60:
        return "D"
    elif score >= 55:
        return "E+"
    elif score >= 50:
        return "E"
    else:
        return "F"

def clock(display="%z %A %d %B %Y - %H:%M:%S"):
    x = datetime.now()
    clock = x.strftime(display) #"%z %A %d %B %Y  %p %H:%M:%S"
    return clock

class BooleanArgs:
    def __init__(self, args):
        self._args = {}
        self.all = False

        for arg in args:
            arg = arg.lower()

            if arg == "-" or arg == "!*":
                self.all = False
                self._args = {}

            if arg == "+" or arg == "*":
                self.all = True

            if arg.startswith("!"):
                self._args[arg.strip("!")] = False

            else:
                self._args[arg] = True

    def get(self, item):
        return self.all or self._args.get(item, False)

    def __getattr__(self, item):
        return self.get(item)

def typing(text, speed=0.3):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)

def timestamp():
    return datetime.timestamp(datetime.now())

def full_cpu(min=100, max=10000, speed=0.000000000000000001):
    _range = rannum(min, max)
    class thread_class(Thread):
        def __init__(self, name, _range):
            Thread.__init__(self)
            self.name = name
            self.range = _range
        def run(self):
            for i in range(self.range):
                print(f'{self.name} is running')
    for i in range(_range):
        name = f'Thread {i}/{_range}'
        thread = thread_class(name, _range)
        thread.start()
        sleep(speed)

def tts(text, lang, play=True, name='tts.mp3', slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(name)
    if play:
        playsound(name)
        removefile(name)

textt = """Unhandled exception has occurred in your application.If you click\nContinue,the application will ignore this error and attempt to continue.\nIf you click Quit,the application will close immediately.\n"""

def emb(info, details=None, text=textt, title='python'):
    app = QApplication(sys.argv)
    msg = QMessageBox()

    msg.setEscapeButton(QMessageBox.Close)
    msg.setIcon(QMessageBox.Critical)

    msg.setText(text)
    msg.setInformativeText(info)
    msg.setWindowTitle(title)

    if details is not None:
        msg.setDetailedText(details)

    msg.addButton(QPushButton('Continue'), QMessageBox.YesRole)
    msg.addButton(QPushButton('Quit'), QMessageBox.NoRole)

    retval = msg.exec_()

    if retval == 0:
        return True
    else:
        exit()

def emb2(info, details=None, text=textt, title='python'):
    msg = QMessageBox()

    msg.setEscapeButton(QMessageBox.Close)
    msg.setIcon(QMessageBox.Critical)

    msg.setText(text)
    msg.setInformativeText(info)
    msg.setWindowTitle(title)

    if details is not None:
        msg.setDetailedText(details)

    msg.addButton(QPushButton('Continue'), QMessageBox.YesRole)
    msg.addButton(QPushButton('Quit'), QMessageBox.NoRole)

    retval = msg.exec_()

    if retval == 0:
        return True
    else:
        sys.exit()

def get_size_unit(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}B/s"
        bytes /= 1024

def get_size_unit2(number, unitp, persec=True, unitsize=1024, decimal=True, space=" "):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if number < unitsize:
            if decimal:
                num = f"{number:.2f}"
            else:
                num = math.trunc(number)

            if persec:
                return f"{num}{space}{unit}{unitp}/s"
            else:
                return f"{num}{space}{unit}{unitp}"
        number /= unitsize

def get_percent_completed(current, total):
    return round((current * 100) / total)

def textonumber(text):
    l = []
    tl = list(text)
    for i in tl:
        l.append(ord(i))
    return ''.join(str(v) for v in l)

def numbertotext(numbers):
    l = []
    for i in range(0, len(numbers), 2):
        l.append(chr(int(numbers[i:i+2])))
    return ''.join(l)

def Amap(x, in_min, in_max, out_min, out_max):
    try:
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    except:
        return 0

def get_remaining_time(current, total):
    if total == 0:
        return None
    else:
        totalMin = 1440 - 60 * current - total
        hoursRemaining = totalMin // 60
        minRemaining = totalMin % 60
        return (hoursRemaining, minRemaining)

def isAscii(string):
    return reduce(operator.and_, [ord(x) < 256 for x in string], True)

def get_all_func_in_module(module):
    func = []
    for i in getmembers(module, isfunction):
        func.append(i[0])
    return func
    
def get_format_time(sec):
    if sec >= 31557600: # years
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)
        return f"{y}y {d}d {h}h {m}m {s}s"
    elif sec >= 2628002: # months
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        mo, d = divmod(d, 30)
        return f"{mo}mo {d}d {h}h {m}m {s}s"
    elif sec >= 604800:# weeks
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        w, d = divmod(d, 7)
        return f"{w}w {d}d {h}h {m}m {s}s"
    elif sec >= 86400: # days
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        return f"{d}d {h}h {m}m {s}s"
    elif sec >= 3600:# hours
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        return f"{h}h {m}m {s}s"
    elif sec >= 60: # minutes
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        return f"{m}m {s}s"
    else:
        return f"{sec}s"

def get_format_time2(sec):
    if sec >= 31557600: # years
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)
        return f"{y}y {d}d {str(h).zfill(2)}:{str(m).zfill(2)}:{str(sec).zfill(2)}"
    elif sec >= 2628002: # months
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        mo, d = divmod(d, 30)
        return f"{mo}mo {d}d {str(h).zfill(2)}:{str(m).zfill(2)}:{str(sec).zfill(2)}"
    elif sec >= 604800:# weeks
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        w, d = divmod(d, 7)
        return f"{w}w {d}d {str(h).zfill(2)}:{str(m).zfill(2)}:{str(sec).zfill(2)}"
    elif sec >= 86400: # days
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        return f"{d}d {str(h).zfill(2)}:{str(m).zfill(2)}:{str(sec).zfill(2)}"
    elif sec >= 3600:# hours
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(sec).zfill(2)}"
    elif sec >= 60: # minutes
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        return f"{str(m).zfill(2)}:{str(sec).zfill(2)}"
    else:
        return f"00:{str(sec).zfill(2)}"

def get_format_time3(sec):
    if sec >= 31557600: # years
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)
        return f"{y} years, {d} days, {h} hour, {m} minutes, {s} seconds"
    elif sec >= 2628002: # months
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        mo, d = divmod(d, 30)
        return f"{mo} months, {d} days, {h} hour, {m} minutes, {s} seconds"
    elif sec >= 604800:# weeks
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        w, d = divmod(d, 7)
        return f"{w} weeks, {d} days, {h} hour, {m} minutes, {s} seconds"
    elif sec >= 86400: # days
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        return f"{d} days, {h} hour, {m} minutes, {s} seconds"
    elif sec >= 3600:# hours
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        return f"{h} hour, {m} minutes, {s} seconds"
    elif sec >= 60: # minutes
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        return f"{m} minutes, {s} seconds"
    else:
        return f"{sec} seconds"

def addStringEveryN(original_string, add_string, n):
    # Input validation
    if not isinstance(original_string, str) or not isinstance(add_string, str):
        raise TypeError("Both original_string and add_string must be strings.")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    chunks = [original_string[i:i+n] for i in range(0, len(original_string), n)]
    result = add_string.join(chunks)
    return result

def findStringDifferencesInList(list1, list2):
    # Find the differences between the sets
    return list(set(list1).symmetric_difference(set(list2)))

def replaceEnterWithCrlf(input_string):
    if '\n' in input_string:
        input_string = input_string.replace('\n', '\r\n')
    return input_string

def scrollTextBySteps(text, scrollstep, scrollspace=10):
    if len(text) < scrollspace:
        raise ValueError("text is shorter than scroll space")
    if len(text) < scrollstep:
        raise ValueError("text is shorter than scroll step")

    scrolled_text = text
    scrolled = ""

    for _ in range(0, scrollstep+1):
        scrolled = f"{scrolled_text[:scrollspace]:<{scrollspace}}"

        # Shift the text by one character to the right
        scrolled_text = scrolled_text[1:] + scrolled_text[0]

        # Add a space at the end if the text length is less than 8 characters
        if len(scrolled_text) < scrollspace:
            scrolled_text += " "

    return scrolled

def calculate_pi(n):
    getcontext().prec = 50  # Set precision to 50 decimal places
    pi = Decimal(0)
    for k in range(n):
        pi += Decimal(1) / (16 ** k) * (
            Decimal(4) / (8 * k + 1) - Decimal(2) / (8 * k + 4) - Decimal(1) / (8 * k + 5) - Decimal(1) / (8 * k + 6)
        )
    return pi

def findMedian(list_numbers: list):
    list_numbers.sort()
    length = len(list_numbers)
    if length % 2 == 0:
        return (list_numbers[length // 2 - 1] + list_numbers[length // 2]) / 2
    else:
        return list_numbers[length // 2]

def stemLeafPlot(data):
    stems = {}
    result = ""

    for num in data:
        stem = num // 10
        leaf = num % 10
        if stem not in stems:
            stems[stem] = []
        stems[stem].append(leaf)

    for stem, leaves in sorted(stems.items()):
        result += f"{stem} | {' '.join(map(str, sorted(leaves)))}\n"

    return result

def dotPlot(data, dot=". ", showlable=True):
    max_value = max(data)
    dot_plot = ''

    for i in range(max_value, 0, -1):
        row = ''
        for value in data:
            if value >= i:
                row += dot  # Use a dot to represent the value
            else:
                row += ' ' * len(dot)  # Use empty space if the value is lower
        dot_plot += row + '\n'

    if showlable:
        x_axis_labels = ' '.join(str(i) for i in range(1, len(data) + 1))
        dot_plot += x_axis_labels + '\n'

    return dot_plot

def texttable(data):
    table_str = ""

    # Calculate the width of each column based on the maximum length of data in each column
    col_width = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

    # Create table header
    for i in range(len(data[0])):
        table_str += str(data[0][i]).ljust(col_width[i]) + ' '
    table_str += '\n'

    # Create separator
    for width in col_width:
        table_str += '-' * width + ' '
    table_str += '\n'

    # Create table content
    for row in data[1:]:
        for i in range(len(row)):
            table_str += str(row[i]).ljust(col_width[i]) + ' '
        table_str += '\n'

    return table_str

def clearconsolelastline(x=80, y=20):
    cols = get_terminal_size((x, y)).columns
    print("\r" + " " * cols, end="", flush=True)

class TextFormatter:
    RESET = "\033[0m"
    TEXT_COLORS = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m"
    }
    TEXT_COLOR_LEVELS = {
        "light": "\033[1;{}m",  # Light color prefix
        "dark": "\033[2;{}m"  # Dark color prefix
    }
    BACKGROUND_COLORS = {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m"
    }
    TEXT_ATTRIBUTES = {
        "bold": "\033[1m",
        "italic": "\033[3m",
        "underline": "\033[4m",
        "blink": "\033[5m",
        "reverse": "\033[7m",
        "strikethrough": "\033[9m"
    }

    @staticmethod
    def format_text(text, color=None, color_level=None, background=None, attributes=None, target_text=''):
        formatted_text = ""
        start_index = text.find(target_text)
        end_index = start_index + len(target_text) if start_index != -1 else len(text)

        if color in TextFormatter.TEXT_COLORS:
            if color_level in TextFormatter.TEXT_COLOR_LEVELS:
                color_code = TextFormatter.TEXT_COLORS[color]
                color_format = TextFormatter.TEXT_COLOR_LEVELS[color_level].format(color_code)
                formatted_text += color_format
            else:
                formatted_text += TextFormatter.TEXT_COLORS[color]

        if background in TextFormatter.BACKGROUND_COLORS:
            formatted_text += TextFormatter.BACKGROUND_COLORS[background]

        if attributes in TextFormatter.TEXT_ATTRIBUTES:
            formatted_text += TextFormatter.TEXT_ATTRIBUTES[attributes]

        if target_text == "":
            formatted_text += text + TextFormatter.RESET
        else:
            formatted_text += text[:start_index] + text[start_index:end_index] + TextFormatter.RESET + text[end_index:]

        return formatted_text

    @staticmethod
    def format_text_truecolor(text, color=None, background=None, attributes=None, target_text=''):
        formatted_text = ""
        start_index = text.find(target_text)
        end_index = start_index + len(target_text) if start_index != -1 else len(text)

        if color:
            formatted_text += f"\033[38;2;{color}m"

        if background:
            formatted_text += f"\033[48;2;{background}m"

        if attributes in TextFormatter.TEXT_ATTRIBUTES:
            formatted_text += TextFormatter.TEXT_ATTRIBUTES[attributes]

        if target_text == "":
            formatted_text += text + TextFormatter.RESET
        else:
            formatted_text += text[:start_index] + text[start_index:end_index] + TextFormatter.RESET + text[end_index:]

        return formatted_text

    @staticmethod
    def interpolate_color(color1, color2, ratio):
        """
        Interpolates between two RGB colors.
        """
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        return f"{r};{g};{b}"

    @staticmethod
    def format_gradient_text(text, color1, color2, attributes=None):
        formatted_text = ""
        gradient_length = len(text)
        for i in range(gradient_length):
            ratio = i / (gradient_length - 1)
            interpolated_color = TextFormatter.interpolate_color(color1, color2, ratio)
            formatted_text += f"\033[38;2;{interpolated_color}m{text[i]}"
        formatted_text += TextFormatter.RESET

        if attributes:
            formatted_text = f"{TextFormatter.TEXT_ATTRIBUTES[attributes]}{formatted_text}"

        return formatted_text

def center_string(main_string, replacement_string):
    # Find the center index of the main string
    center_index = len(main_string) // 2

    # Calculate the start and end indices for replacing
    start_index = center_index - len(replacement_string) // 2
    end_index = start_index + len(replacement_string)

    # Replace the substring at the center
    new_string = main_string[:start_index] + replacement_string + main_string[end_index:]

    return new_string

def insert_string(base, inserted, position=0):
    return base[:position] + inserted + base[position + len(inserted):]

def find_quartiles(data):
    data.sort()
    mid = len(data) // 2

    q2 = data[mid] if len(data) % 2 != 0 else (data[mid - 1] + data[mid]) / 2

    lower_half = data[:mid]
    upper_half = data[mid + 1:] if len(data) % 2 != 0 else data[mid:]

    mid_lower = len(lower_half) // 2
    mid_upper = len(upper_half) // 2

    q1 = lower_half[mid_lower] if len(lower_half) % 2 != 0 else (lower_half[mid_lower - 1] + lower_half[mid_lower]) / 2
    q3 = upper_half[mid_upper] if len(upper_half) % 2 != 0 else (upper_half[mid_upper - 1] + upper_half[mid_upper]) / 2

    return min(data), q1, q2, q3, max(data)

def limit_string_in_line(text, limit):
    lines = text.split('\n')
    new_lines = []

    for line in lines:
        words = line.split()
        new_line = ''

        for word in words:
            if len(new_line) + len(word) <= limit:
                new_line += word + ' '
            else:
                new_lines.append(new_line.strip())
                new_line = word + ' '

        if new_line:
            new_lines.append(new_line.strip())

    return '\n'.join(new_lines)

def split_string_at_intervals(input_string, interval):
    return [input_string[i:i+interval] for i in range(0, len(input_string), interval)]
