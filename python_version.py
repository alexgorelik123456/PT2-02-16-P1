import sys

def python_ver():
    version_of_python = sys.version_info[:3]
    if version_of_python[0] == 2:
        print('Python 2.x')
    else:
        print('Python 3.x')

python_ver()
