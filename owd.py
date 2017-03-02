# 터미널에서 이 스크립트를 실행시키면 현재 위치(Working directory)로 탐색기를 열어준다

import os
import subprocess

path = os.getcwd()
print (path)
subprocess.call('explorer "%s"' % path, shell = True)
