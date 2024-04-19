import argparse
from . import saying

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="a happy cow")
    parser.add_argument("--word", default="mooo")
    args = parser.parse_args()
    print(saying(args.name, args.word))