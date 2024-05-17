from argparse import ArgumentParser
from math import sqrt


def parseArgs():
    parser = ArgumentParser()
    parser.add_argument("-t", "--text", dest="text",
                        help="the text displayed inside the heart")
    return parser.parse_args()


def evaluateHeartCurve(x, y):
    return pow(x, 2) + pow(y-sqrt(abs(x)), 2)


def replaceCentered(text, line):
    start = (len(line) - len(text)) // 2 + 1
    return line[0: start] + text + line[start + len(text):]


def printHeart(text):
    for y in range(-15, 12):
        line = ''
        for x in range(-25, 25):
            value = evaluateHeartCurve(x / 12, -y / 5)
            line += '+' if (abs(value - 3) < 0.6) else ' '
        if (y == -4):
            line = replaceCentered(text, line)
        print(line)


if __name__ == "__main__":
    args = parseArgs()
    printHeart(args.text or "")
