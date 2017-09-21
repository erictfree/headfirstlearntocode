def make_crazy_lib(filename):
    file = open(filename, 'r')

    text = ''

    for line in file:
        text = text + process_line(line) 

    file.close()

    return text

def process_line(line):
    return line

def main():
    lib = make_crazy_lib('lib.txt')
    print(lib)

if __name__ == '__main__':
    main()
