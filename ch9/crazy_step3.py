def make_crazy_lib(filename):
    file = open(filename, 'r')

    text = ''

    for line in file:
        text = text + process_line(line) 

    file.close()

    return text

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

def main():
    lib = make_crazy_lib('lib.txt')
    print(lib)

if __name__ == '__main__':
    main()
