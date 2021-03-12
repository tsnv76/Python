import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("a", nargs='?', default=0)
parser.add_argument("b", nargs='?', default=0)
args = parser.parse_args()
num1 = int(args.a)-1
num2 = int(args.b)

file_path = 'bakery.csv'

with open(file_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if num2 == 0 and i >= num1:
            print(line.strip())
        if i in range(num1, num2):
            print(line.strip())
