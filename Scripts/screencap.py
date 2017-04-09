import sys
import subprocess

OPTION = ''
IMAGE_OUTPUT_PATH = ''

if len(sys.argv) == 2:
    IMAGE_OUTPUT_PATH = sys.argv[1]
    
elif len(sys.argv) == 3:
    OPTION = sys.argv[1]
    IMAGE_OUTPUT_PATH = sys.argv[2]
    
else:
    print('screencap [-option] <img_output_path>')
    sys.exit()

TMP_DIR = '/sdcard/_tmp1234567/'

# 기기 안에 사진을 임시 저장할 디렉토리 생성
if subprocess.run("adb %s shell mkdir %s" % (OPTION, TMP_DIR)).returncode != 0:
    print('error!')
    sys.exit()

# 기기 안에 사진 캡쳐
if subprocess.run("adb %s shell screencap -p %s" % (OPTION, TMP_DIR + IMAGE_OUTPUT_PATH)).returncode != 0:
    print('error!')
    sys.exit()
    
# 기기 안에 저장된 사진을 데스크탑으로 가져오기
if subprocess.run("adb %s pull %s" % (OPTION, TMP_DIR + IMAGE_OUTPUT_PATH)).returncode != 0:
    print('error!')
    sys.exit()

# 임시 사진 삭제
if subprocess.run("adb %s shell rm -rf %s" % (OPTION, TMP_DIR)).returncode != 0:
    print('error!')
    sys.exit()