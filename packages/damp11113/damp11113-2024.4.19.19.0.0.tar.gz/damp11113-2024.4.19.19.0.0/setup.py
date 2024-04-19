from setuptools import setup, find_packages
import platform

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Common dependencies for all platforms
common_dependencies = [
    "dearpygui",
    "iso-639",
    "numpy",
    "scipy",
    "natsort",
    "psutil",
    "Pillow",
    "blend-modes",
    "opencv-python",
    "libscrc",
    "PyAudio",
    "python-vlc",
    "ffmpeg-python",
    "yt-dlp",
    "youtube_dl",
    "pafy",
    "pafy2"
    "tqdm",
    "qrcode",
    "python-barcode",
    "pydub",
    "pyzbar",
    "mcstatus",
    "mcrcon",
    "paho-mqtt",
    "requests",
    "pymata-aio",
    "six",
    "key-generator",
    "PyQt5",
    "gTTS",
    "py-cpuinfo",
    "GPUtil",
    "playsound"
]

# Windows-specific dependencies
windows_dependencies = [
    "pywin32",
    "win32gui",
    "comtypes",
]

# List of files to exclude based on the operating system
exclude_files_windows = [
    "src/damp11113/pywindows.py",
]

# Add platform-specific dependencies
if platform.system() == 'Windows':
    install_requires = common_dependencies + windows_dependencies
    dependency_links = [
        'git+https://github.com/damp11113/pafy2.git#egg=pafy2'
    ]
else:
    install_requires = common_dependencies
    dependency_links = [
        'git+https://github.com/damp11113/pafy2.git#egg=pafy2'
    ]

    # Exclude files for non-Windows platforms
    package_data = {
        '': exclude_files_windows,
    }

setup(
    name='damp11113',
    version='2024.4.19.19.0.0',
    license='MIT',
    author='damp11113',
    author_email='damp51252@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/damp11113/damp11113-library',
    description="A Utils library and Easy to using.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    dependency_links=dependency_links,
    package_data=package_data if 'package_data' in locals() else {},
)