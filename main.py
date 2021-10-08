import sys

from fontTools import ttLib
from opencc_t2s import OpenCC_T2S


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def deal(path: str):
    # Use a breakpoint in the code line below to debug your script.
    print(path)
    f = ttLib.TTFont(path)
    cmap = f.getBestCmap()
    for t, s in OpenCC_T2S.items():
        s_key = ord(s)
        t_key = ord(t)
        if s_key in cmap:
            cmap[t_key] = cmap[s_key]
    # print(ord("你"))
    # for char in sorted(cmap):
    #     print("%s=>%s" % (char, chr(char)))
    # pass
    f.save("test.ttf")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    deal(sys.argv[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
