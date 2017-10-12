import sys

def make_crazy_lib(filename):
    try:
        file = open(filename, 'r')

        text = ''

        for line in file:
            text = text + process_line(line) 

        file.close()

        return text

    except FileNotFoundError:
        print("Sorry, couldn't find", filename + '.')
    except IsADirectoryError:
        print("Sorry", filename, 'is a directory.')
    except:
        print("Sorry, could not read", filename)

placeholders = ['NOUN', 'ADJECTIVE', 'VERB_ING', 'VERB']

def process_line(line):
    global placeholders

    processed_line = ''

    words = line.split()

    for word in words:
        stripped = word.strip('.,;?!')
        if stripped in placeholders:
            answer = input('Enter a ' + stripped + ":")
            processed_line = processed_line + answer
            if word[-1] in '.,;?!':
                processed_line = processed_line + word[-1] + ' '
            else:
                processed_line = processed_line + ' '
        else:
            processed_line = processed_line + word + ' '
    return processed_line + '\n'

def save_crazy_lib(filename, text):
    try:
        file = open(filename, 'w')
        file.write(text)
        file.close()
    except:
        print("Sorry, couldn’t write file.", filename)

def main():
    if len(sys.argv) != 2:
        print("crazy.py <filename>")
    else:
        filename = sys.argv[1]
        lib = make_crazy_lib(filename)
        if (lib != None):
            save_crazy_lib('crazy_' + filename, lib)

if __name__ == '__main__':
    main()
