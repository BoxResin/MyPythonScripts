import os
import subprocess

path = os.getcwd()
print (path)
subprocess.call('explorer "%s"' % path, shell = True)
