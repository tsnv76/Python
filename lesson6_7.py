import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("a", nargs='?', default=1)
parser.add_argument("b", nargs='?', default=5555.55)
args = parser.parse_args()
pos = int(args.a)-1
new_num = str(args.b)

print(pos, new_num)

file_path = 'bakery.csv'
with open(file_path, 'r+', encoding='utf-8') as f:
    line = f.readline()
    count = 0
    if pos == count:
        f.seek(0)
        f.write(f'{new_num}\n')
        raise SystemExit(0)
    if line == '':
        f.seek(2)
        f.write(f'{new_num}\n')
    while line:
        count += 1
        if count == pos:
            num_line = f.tell()
            f.seek(num_line,0)
            if len(str(num_line)) >= len(line) and line != '':
                new_num +='\n'
            f.write(f'{new_num}')
            num_line = f.tell()
            raise SystemExit(0)
        line = f.readline()
print('Вы ввели несуществующую запись')
