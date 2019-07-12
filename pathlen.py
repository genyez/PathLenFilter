import os
import sys

maxlen = 255

def work():
    outlist = []
    filecount = 0
    for root ,dirs, files in os.walk(os.path.curdir):
        for file in files:
            filecount += 1
            print("searched file: %d" % filecount)
            fullpath = os.path.join(os.path.abspath(root), file)
            if len(fullpath) > maxlen:
                outlist.append(fullpath)
    return outlist

def main():
    global maxlen
    if len(sys.argv) > 1:
        try:
            maxlen = int(sys.argv[1])
        except:
            pass
    outlist = work()
    with open("result.txt", "wt") as f:
        f.write("\n".join(outlist))

if __name__ == '__main__':
    main()