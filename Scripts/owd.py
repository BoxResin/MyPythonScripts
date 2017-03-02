"""
터미널에서 이 스크립트를 실행시키면 현재 위치(Working directory)로 탐색기를 열어준다

사용법
$ python owd.py
현재 Working directory를 탐색기에서 연다.
"""

import os
import subprocess

path = os.getcwd()
print(path)
subprocess.call('explorer "%s"' % path, shell = True)
