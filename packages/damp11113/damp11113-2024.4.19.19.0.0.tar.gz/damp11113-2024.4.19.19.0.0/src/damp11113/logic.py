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

def AND(in1=False, in2=False):
    if in1 is True:
        if in2 is True:
            return True
        else:
            return False
    else:
        return False

def NOT(in1=False):
    if in1 is False:
        return True
    else:
        return False

def NAND(in1=False, in2=False):
    return NOT(AND(in1, in2))

def OR(in1=False, in2=False):
    return NAND(NOT(in1), NOT(in2))

def XOR(in1, in2):
    OOR = OR(in1, in2)
    ONAND = NAND(in1, in2)
    return AND(OOR, ONAND)

def ADDER(in1=False, in2=False, in3=False):
    OXOR = XOR(in1, in2)
    OAND = AND(in1, in2)
    OXOR2 = XOR(OXOR, in3)
    OAND2 = AND(OXOR, in3)
    OOR = OR(OAND2, OAND)
    return (OXOR2, OOR)

def ADDER_4BIT(in1=False, in2=False, in3=False, in4=False, in5=False, in6=False, in7=False, in8=False, in9=False):
    OADDER11, OADDER12 = ADDER(in4, in8, in9)
    OADDER21, OADDER22 = ADDER(in3, in7, OADDER12)
    OADDER31, OADDER32 = ADDER(in2, in6, OADDER22)
    OADDER41, OADDER42 = ADDER(in1, in5, OADDER32)
    return (OADDER41, OADDER31, OADDER21, OADDER11, OADDER42)

def ALU(in1=False, in2=False, in3=False, in4=False, in5=False, in6=False, in7=False, in8=False, in9=False):
    OXOR1 = XOR(in5, in9)
    OXOR2 = XOR(in6, in9)
    OXOR3 = XOR(in7, in9)
    OXOR4 = XOR(in8, in9)
    a4b1, a4b2, a4b3, a4b4, a4b5 = ADDER_4BIT(in1, in2, in3, in4, OXOR1, OXOR2, OXOR3, OXOR4, in9)
    ONOT1 = NOT(a4b1)
    ONOT2 = NOT(a4b2)
    ONOT3 = NOT(a4b3)
    ONOT4 = NOT(a4b4)
    OAND1 = AND(ONOT1, ONOT2)
    OAND2 = AND(OAND1, ONOT3)
    OAND3 = AND(OAND2, ONOT4)
    return (a4b1, a4b2, a4b3, a4b4, a4b5, a4b1, OAND3)