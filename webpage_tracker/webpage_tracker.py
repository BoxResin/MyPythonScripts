# 웹페이지 내용이 바뀌었는지 추적하는 스크립트
# 첫 번째 Argument를 url로 간주하여 웹페이지의 변화가 감지되었을 경우 알림을 보낸다.

import sys
import hashlib
import time
import ctypes
import webbrowser
from urllib.request import Request, urlopen

if len(sys.argv) > 1:
    url = sys.argv[1]

    while True:
        # content: 웹 페이지 문서 내용 (bytes)
        content = urlopen(Request(url)).read()

        # print(content.decode(encoding = 'euc-kr', errors = 'ignore'))
        current = hashlib.md5(content).hexdigest()

        try:
            f = open('cache.txt')
            last = f.read()
            f.close()

            if current != last:
                MessageBox = ctypes.windll.user32.MessageBoxW
                if MessageBox(None, '웹페이지가 바뀌었습니다! 변경된 내용을 보시겠습니까?', '알림', 4) == 6:
                    webbrowser.open(url)
                raise Exception('The webpage has been changed!')

        except Exception as e:
            # 해시 값을 저장한다.
            f = open('cache.txt', mode = 'w')
            f.write(current)
            f.close()

        time.sleep(30 * 60)
