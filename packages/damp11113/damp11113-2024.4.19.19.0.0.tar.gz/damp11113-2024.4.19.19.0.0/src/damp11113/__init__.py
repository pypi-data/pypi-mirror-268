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

import os
import platform
from .info import __version__

try:
    os.environ["damp11113_load_all_module"]
except:
    os.environ["damp11113_load_all_module"] = "YES"

if os.environ["damp11113_load_all_module"] == "YES":
    if platform.system() == "Windows":
        from .pywindows import *
        from .OPFONMW.dearpygui_animate import *
        from .OPFONMW.ofdm_codec import *

    from .info import *
    from .file import *
    from .network import *
    from .randoms import *
    from .processbar import *
    from .media import *
    from .convert import *
    from .imageps import *
    from .utils import *
    from .minecraft import *
    from .plusmata import *
    from .imageps import *
    from .DSP import *
    from .logic import *

try:
    os.environ["damp11113_check_update"]
except:
    os.environ["damp11113_check_update"] = "YES"

if os.environ["damp11113_check_update"] == "YES":
    from pygments import console
    import requests
    print(console.colorize("yellow", "library check update..."))
    try:
        response = requests.get(f"https://cdn.damp11113.xyz/file/text/damp11113libver.txt")
        if response.status_code == 200:
            if response.text == __version__:
                print(f'{console.colorize("green", "no update available")}')
                print(f'{console.colorize("green", f"library version current: {__version__}")}')
            else:
                print(console.colorize("yellow", "update available"))
                print(f'{console.colorize("green", f"library version current: {__version__}")}')
                print(f'{console.colorize("green", f"new: {response.text}")}')
        else:
            print(f'{console.colorize("red", f"check update failed. please try again (error {response.status_code})")}')
            print(f'{console.colorize("yellow", f"library version current: {__version__}")}')

    except:
        print(console.colorize("red", "check update failed. please try again"), f'{__version__}')
        print(f'{console.colorize("yellow", f"library version current: {__version__}")}')