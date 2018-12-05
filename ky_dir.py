import os
import sys
import json
from pathlib import Path


def do_logic(target_path=os.getcwd()):
    result = {}

    for t in [f for f in Path(target_path).glob('**/*') if os.path.isfile(f)]:
        try:
            result[str(t)] = {
                'file_name': os.path.basename(t),
                'dir_name': os.path.dirname(t),
                'file_size': os.path.getsize(t),
                'lines': sum(1 for _ in open(t))
            }
        except UnicodeDecodeError:
            print('file: {} {}'.format(t, sys.exc_info()))

    return result


if __name__ == '__main__':
    for key, value in do_logic().items():
        print(value)
