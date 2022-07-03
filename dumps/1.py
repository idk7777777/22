import os
import shutil

i = 0
dir_path = os.path.dirname(os.path.realpath(__file__))
output = [dI for dI in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path,dI))]
print(output)
print(dir_path)

while (i < len(output)):
    try:
        dirr = (dir_path + '/' + output[i])
        size = (os.path.getsize(dir_path + '/' + output[i] + "/log"))
        print(size)
        print(output[i])
        if size < 700000:
            shutil.rmtree(dirr)
    except:
        print("ERR")
    i = i + 1
