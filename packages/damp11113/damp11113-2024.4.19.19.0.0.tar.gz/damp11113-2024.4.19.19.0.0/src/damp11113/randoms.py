"""
damp11113-library - A Utils library and Easy to use. For more info visit https://github.com/damp11113/damp11113-library/wiki
Copyright (C) 2021-2023 damp11113 (MIT)

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

import random
import string
import uuid
from .convert import list2str2

def rannum(number1, number2):
    try:
        return random.randint(int(number1), int(number2))
    except ValueError:
        print("Please enter a number1 to number2")

def rannumfloat(number1, number2):
    try:
        return random.uniform(number1, number2)
    except ValueError:
        print("Please enter a number1 to number2")

def ranstr(charset):
    try:
        char_set = string.ascii_uppercase + string.digits
        output = ''.join(random.sample(char_set * int(charset), int(charset)))
        return output
    except ValueError:
        print("Please enter a number charset")

def ranuuid(uuid_type='uuid1'):
    if uuid_type == "uuid1":
        return uuid.uuid1()
    elif uuid_type == "uuid4":
        return uuid.uuid4()
def ranchoice(list):
    try:
        output = random.choice(list)
        return output
    except ValueError:
        print("Please enter a list")

def ranshuffle(list):
    try:
        output = random.shuffle(list)
        return output
    except ValueError:
        print("Please enter a list")

def ranrandrange(number1, number2):
    try:
        output = random.randrange(number1, number2)
        return output
    except ValueError:
        print("Please enter a number1 to number2")

def rancolor():
    """RGB"""
    return (rannum(1, 255), rannum(1, 255), rannum(1, 255))

def rantextuplow(text):
    nct = list(text)
    ct = []
    for i in nct:
        r = rannum(1, 2)
        if r == 1:
            ct.append(str(i).lower())
        elif r == 2:
            ct.append(str(i).upper())
    return list2str2(ct)

def ranstruplow(charset):
    return rantextuplow(ranstr(charset))

def randistro():
    return f'https://discord.gift/{ranstruplow(23)}'

def ranlossbin(codeword, error_rate):
    # Convert the error rate to a number of errors to introduce
    num_errors = int(len(codeword) * error_rate)

    # Randomly select bit indices to flip
    error_indices = random.sample(range(len(codeword)), num_errors)

    # Flip the selected bits
    received_codeword = list(codeword)
    for index in error_indices:
        received_codeword[index] = '1' if received_codeword[index] == '0' else '0'

    return ''.join(received_codeword)


def ranlossbytes(data, loss_percentage):
    if not 0 <= loss_percentage <= 100:
        raise ValueError("Loss percentage should be between 0 and 100")

    num_bytes_to_drop = int(len(data) * (loss_percentage / 100))
    indices_to_drop = random.sample(range(len(data)), num_bytes_to_drop)

    result = bytearray()
    for i, byte in enumerate(data):
        if i not in indices_to_drop:
            result.append(byte)

    return bytes(result)

def rannumlist(number1, number2, maxrange):
    return [random.randint(number1, number2) for _ in range(maxrange)]

def generate_binary_combinations(width):
    binarys = []
    total_combinations = 2 ** width
    for i in range(total_combinations):
        binarys.append(format(i, '0' + str(width) + 'b'))
    return binarys