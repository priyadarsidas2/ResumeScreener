import os
import glob
from pathlib import Path

def deleteOutputFiles():
    p = Path(__file__).parents[2]
    path = str(p)+ "\\" + "output" + "\\*"
    files = glob.glob(path)
    #print(path)
    #print(files)
    for f in files:
        os.remove(f)
    #print("cleaned")
    return

#if __name__ == '__main__':
#    deleteOutputFiles()
