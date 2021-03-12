import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("a", default='0')
args = parser.parse_args()
num = args.a
file_path = 'bakery.csv'

with open(file_path, 'a', encoding='utf-8') as f:
    f.write(f'{num} \n')
