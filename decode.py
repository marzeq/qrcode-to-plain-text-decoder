import pip
import sys
import os
import time
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try:
    import cv2
    import wget
except ImportError:
    print("----------\nInstalling vital packages!\n----------")
    time.sleep(3)
    install("opencv-python")
    install("wget")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n----------\nRerun the code!\n----------")
    time.sleep(5)
    quit()


sys.argv.pop(0)
url = sys.argv[0]
if len(sys.argv) > 1:
    tofile = True
    tofilepath = sys.argv[1]
else:
    tofile = False

downloaded = wget.download(url)
img = cv2.imread(downloaded)

qrdetector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = qrdetector.detectAndDecode(img)
if bbox is not None: print(f"\n{data}")
if bbox is not None and tofile:
    with open(tofilepath, "w") as file: file.write(data) # noqa

os.remove(downloaded)
