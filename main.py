from ctypes import *

func = CDLL("./func.so")

if __name__ == "__main__":
    print(1000)