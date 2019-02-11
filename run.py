import sys,os
from gen import genMap, mapNode

TEST_DIR = os.path.join(".",os.path.join("test"))

def main(argv):
    if len(argv) < 1:
        print("Usage:")
        print("python run.py <number>")
    else:
        num = argv[0]
        run = genMap()
        run.test(TEST_DIR,num)
    pass
 
if __name__ == "__main__":
   main(sys.argv[1:])
   a = 1
